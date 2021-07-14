from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from Textile_Market.textile_profile.forms import ProfileForm
from Textile_Market.textile_profile.models import Profile


def profile(request):
    if request.user.is_superuser:
        profiles = Profile.objects.all()
    else:
        profiles = [request.user.profile]
    context = {
        'profiles': profiles,
    }
    return render(request, 'profile.html', context)


def update_profile(request, pk):
    wrong_credentials = False
    profile = Profile.objects.get(pk=pk)
    user = profile.user
    user_form = UserCreationForm(instance=user)
    profile_form = ProfileForm(instance=profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'wrong_credentials': wrong_credentials
    }
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password2']
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            groups = Group.objects.all()
            for group in groups:
                user.groups.remove(group)
            for group in groups:
                if group.name == 'User' and profile.type == 'person':
                    user.groups.add(group)
                if group.name == 'Company' and profile.type == 'company':
                    user.groups.add(group)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            return redirect('login')
        else:
            context['wrong_credentials'] = True
            return render(request, 'profile_update.html', context)
    return render(request, 'profile_update.html', context)


def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    user = profile.user
    user_form = UserCreationForm(instance=user)
    profile_form = ProfileForm(instance=profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile
    }
    if request.method == 'GET':
        for form in [user_form, profile_form]:
            for field in form.fields:
                form.fields[field].widget.attrs['readonly'] = True
                form.fields[field].widget.attrs['disabled'] = True
        return render(request, 'delete_profile.html', context)
    user.delete()
    profile.delete()
    return redirect('home')
