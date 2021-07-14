from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from Textile_Market.textile_auth.forms import LoginForm
from Textile_Market.textile_profile.forms import ProfileForm
from Textile_Market.textile_profile.models import Profile


def login_view(request):
    wrong_credentials = False
    form = LoginForm()
    context = {
        'form': form,
        'wrong_credentials': wrong_credentials
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_superuser:

                    if len(Profile.objects.filter(user=user)) == 0:
                        profile = Profile(user=user, first_name='SUPERUSER').save()
                        login(request, user)
                        return redirect('profile')
                login(request, user)
                return redirect('home')
            else:
                context['wrong_credentials'] = True
                return render(request, 'login.html', context)
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    wrong_credentials = False
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'wrong_credentials': wrong_credentials
    }
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password2']
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
        else:
            context['wrong_credentials'] = True
            return render(request, 'register.html', context)
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
