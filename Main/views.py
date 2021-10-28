from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Main.forms import LoginForm


def main(request):
    return render(request, 'Main/main-page.html')


def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')

    return render(request, 'Main/login.html', locals())
