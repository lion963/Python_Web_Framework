from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from Textile_Market.textile_auth.forms import LoginForm, ProfileRegisterForm
from Textile_Market.textile_profile.models import Profile


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'app_auth/login.html', context)

    form = LoginForm(request.POST)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_superuser:
                if len(Profile.objects.filter(user=user)) == 0:
                    profile = Profile(user=user, first_name='SUPERUSER').save()
                    login(request, user)
                    return redirect('home')
            login(request, user)
            return redirect('home')
    return render(request, 'app_auth/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'GET':
        user_form = UserCreationForm()
        profile_form = ProfileRegisterForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'app_auth/register.html', context)

    user_form = UserCreationForm(request.POST)
    profile_form = ProfileRegisterForm(request.POST, request.FILES)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    if user_form.is_valid() and profile_form.is_valid():
        username = user_form.cleaned_data['username']
        password = user_form.cleaned_data['password2']
        user = user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        groups = Group.objects.all()
        for group in groups:
            if group.name == 'User' and profile.type == 'person':
                user.groups.add(group)
            if group.name == 'Company' and profile.type == 'company':
                user.groups.add(group)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'app_auth/register.html', context)





