from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

from .decorators import allowed_groups
from .forms import PythonCreateForm, LoginForm, RegisterForm
from .models import Python



def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})



@login_required(login_url='login')
@allowed_groups(['User'])
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')

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
    form = RegisterForm()
    context = {'form': form}
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password)
            groups = Group.objects.all()
            for group in groups:
                if group.name == 'User':
                    user.groups.add(group)
            return redirect('index')
    return render(req, 'register.html', context)


def logout_view(req):
    logout(req)
    return redirect('index')

def page_401(req):
    return render(req, '401_page.html')


