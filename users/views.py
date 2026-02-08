from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data= request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'Вы вошли в аккаунт как  {username}')
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form,
    }
    return render(request,'users/login.html', context=context)

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'Вы успешно зарегестрировались как  {user.username}')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form,
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Профайл успешно обновлён ')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')

@login_required
def logout(request):
    messages.success(request, f' {request.user.username} Успешно вышел из аккаунта')
    auth.logout(request)
    return redirect(reverse('users:login'))