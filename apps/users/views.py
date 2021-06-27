from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login


def login(request):
    return render(request, 'users/login.html')


def signup(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})
