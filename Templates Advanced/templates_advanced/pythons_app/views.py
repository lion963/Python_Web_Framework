from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView

from .decorators import allowed_groups
from .forms import PythonCreateForm, LoginForm, UserForm, ProfileForm
from .mixins import GroupRequiredMixin
from .models import Python, Profile


# def index(req):
#     pythons = Python.objects.all()
#     return render(req, 'index.html', {'pythons': pythons})

class IndexView(ListView):
    context_object_name = 'pythons'
    model = Python
    template_name = 'index.html'


# @login_required(login_url='login')
# @allowed_groups(['User'])
# def create(req):
#     if req.method == 'GET':
#         form = PythonCreateForm()
#         return render(req, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(req.POST, req.FILES)
#         if form.is_valid():
#             python = form.save()
#             python.save()
#             return redirect('index')


class CreatePythonView(GroupRequiredMixin, FormView):
    template_name = 'create.html'
    success_url = '/'
    form_class = PythonCreateForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    group_required = ['User']


# class RegisterView(CreateView):
#     model = Profile
#     form_class = ProfileForm
#     success_url = 'index.html'
#     template_name = 'register.html'


def login_view(req):
    form = LoginForm()
    context = {'form': form}
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user:
                login(req, user)
                return redirect('index')
    return render(req, 'login.html', context)

def register_view(req):
    user_form = UserForm()
    profile_form = ProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    if req.method == 'POST':
        user_form = UserForm(req.POST)
        profile_form = ProfileForm(req.POST, req.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            groups = Group.objects.all()
            for group in groups:
                if group.name == 'User':
                    user.groups.add(group)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('index')
        else:
            print(user_form.errors, profile_form.errors)
    return render(req, 'register.html', context)


def profile_view(request):
    # user_form = UserForm(instance=request.user)
    # profile_form = ProfileForm(instance=request.user.profile)
    user = request.user
    profile = request.user.profile
    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'profile.html', context)

def update_profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    return render(request, 'profile_update.html', context)


# def register_view(req):
#     form = RegisterForm()
#     context = {'form': form}
#     if req.method == 'POST':
#         form = LoginForm(req.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # email = form.cleaned_data['email']
#             user = User.objects.create_user(username=username, password=password)
#             groups = Group.objects.all()
#             for group in groups:
#                 if group.name == 'User':
#                     user.groups.add(group)
#             return redirect('index')
#     return render(req, 'register.html', context)


def logout_view(req):
    logout(req)
    return redirect('index')

def page_401(req):
    return render(req, '401_page.html')


