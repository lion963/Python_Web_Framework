from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView

from Textile_Market.textile_auth.forms import ProfileRegisterForm
from Textile_Market.textile_profile.forms import ProfileForm
from Textile_Market.textile_profile.models import Profile


# def profile(request):
#     if request.user.is_superuser:
#         profiles = Profile.objects.all()
#     else:
#         profiles = [request.user.profile]
#     context = {
#         'profiles': profiles,
#     }
#     return render(request, 'app_profile/profile.html', context)


class ProfileView(ListView):
    model = Profile
    template_name = 'app_profile/profile.html'
    context_object_name = 'profiles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['profiles'] = context['profiles']
        else:
            context['profiles'] = context['profiles'].filter(pk=self.request.user.profile.id)
        return context


# def update_profile(request, pk):
#     if request.method == 'GET':
#         profile = Profile.objects.get(pk=pk)
#         user = profile.user
#         user_form = UserCreationForm(instance=user)
#         profile_form = ProfileForm(instance=profile)
#         context = {
#             'user_form': user_form,
#             'profile_form': profile_form,
#             'profile': profile,
#         }
#         return render(request, 'app_profile/profile_update.html', context)
#
#     profile = Profile.objects.get(pk=pk)
#     user = profile.user
#     user_form = UserCreationForm(request.POST, instance=user)
#     profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
#     context = {
#         'user_form': user_form,
#         'profile_form': profile_form,
#         'profile': profile,
#     }
#     if user_form.is_valid() and profile_form.is_valid():
#         user = user_form.save()
#         username = user_form.cleaned_data['username']
#         password = user_form.cleaned_data['password2']
#         profile = profile_form.save(commit=False)
#         profile.user = user
#         profile.save()
#         groups = Group.objects.all()
#         for group in groups:
#             user.groups.remove(group)
#         for group in groups:
#             if group.name == 'User' and profile.type == 'person':
#                 user.groups.add(group)
#             if group.name == 'Company' and profile.type == 'company':
#                 user.groups.add(group)
#         if request.user.is_superuser:
#             return redirect('profile')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('profile')
#     return render(request, 'app_profile/profile_update.html', context)


class UpdateProfileView(UpdateView):
    template_name = 'app_profile/profile_update.html'
    model = Profile
    fields = '__all__'
    user_form_class = UserCreationForm
    profile_form_class = ProfileRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=context['profile'].user_id)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        if self.request.method == 'GET':
            user_form = self.user_form_class(instance=user)
            profile_form = self.profile_form_class(instance=profile)
        else:
            user_form = self.user_form_class(self.request.POST, instance=user)
            profile_form = self.profile_form_class(self.request.POST, self.request.FILES,instance=profile)
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return context


    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        profile = Profile.objects.get(pk=kwargs['pk'])
        user_form = self.user_form_class(request.POST, instance=user)
        profile_form = self.profile_form_class(request.POST, request.FILES,instance=profile)
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
                return HttpResponseRedirect(self.get_success_url())
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('profile')


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
        return render(request, 'app_profile/delete_profile.html', context)
    user.delete()
    profile.delete()
    return redirect('home')
