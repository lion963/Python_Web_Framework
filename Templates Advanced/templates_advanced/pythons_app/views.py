from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .decorators import allowed_groups
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})

@allowed_groups(['User'])
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        data = req.POST
        form = PythonCreateForm(data, req.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')

def login_view(req):
    user = authenticate(req, username='pesho', password='D22p41570_')
    if user:
        login(req, user)
        return redirect('index')

def logout_view(req):
    logout(req)
    return redirect('index')

def page_401(req):
    return render(req, '401_page.html')


