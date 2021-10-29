from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Main.forms import LoginForm, RegistrationForm


def main(request):
    return render(request, 'Main/main-page.html')


def auth_user(request, form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('/')


def login_user(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    return render(request, 'Main/login.html', locals())


def registration_user(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main')
    return render(request, 'Main/registration.html', locals())
