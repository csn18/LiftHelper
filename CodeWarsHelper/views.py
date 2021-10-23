from django.contrib.sites import requests
from django.shortcuts import render, redirect

from CodeWarsHelper.forms import MemberForm
from CodeWarsHelper.models import CodeWarsTasks, Members, Group


def main_members(request):
    # Get all groups
    groups = Group.objects.all()

    # Add new user form
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group')
    return render(request, 'CodeWars/members.html', locals())


def group_detail(request, pk):
    members = Members.objects.filter(member_group=pk).order_by('-progress')

    return render(request, 'CodeWars/group_detail.html', locals())


def member_detail(request, pk):
    # Get user object
    member = Members.objects.get(id=pk)
    code_wars_username = member.code_wars_username
    all_tasks = CodeWarsTasks.objects.all()
    all_tasks = [task.id_task for task in all_tasks]

    # Get data of user
    response = requests.get(
        f'https://www.codewars.com/api/v1/users/{code_wars_username}/code-challenges/completed').json()
    all_competed_id = [item.get('id') for item in [i for i in response['data']]]
    completed_tasks = [task for task in all_tasks if task in all_competed_id]
    progress = round((len(completed_tasks) / len(all_tasks)) * 100, 1)

    # Save user progress
    member.progress = progress
    member.save()

    return render(request, 'CodeWars/member_detail.html', locals())
