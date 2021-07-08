from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Textile_Market.textile_app.forms import OfferForm, UserForm, ProfileForm, LoginForm
from Textile_Market.textile_app.models import AddOffer


def home_page(request):
    return render(request, 'home_page.html')

def about_us(request):
    return render(request, 'about_us.html')

def offers(request):
    offers = AddOffer.objects.all()
    context = {
        'offers': offers
    }
    return render(request, 'offers.html', context)

def my_offers(request):
    pass

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
                return redirect('home')
    return render(req, 'login.html', context)

@login_required(login_url='login')
def create_offer(request):
    if request.method == 'GET':
        form = OfferForm()
        return render(request, 'create_offer.html', {'form':form})
    form = OfferForm(request.POST, request.FILES)
    if form.is_valid():
        offer = form.save()
        offer.save()
        return redirect('offers')
    return render(request, 'create_offer.html', {'form':form})

def offer_details(request):
    return render(request, 'offer_detail.html')

def register(req):
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
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('home')
        else:
            print(user_form.errors, profile_form.errors)
    return render(req, 'register.html', context)

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
            username = user.username
            password = user.password
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('profile')
    return render(request, 'profile_update.html', context)

def profile(request):
    user = request.user
    profile = request.user.profile
    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'profile.html', context)


def logout_view(req):
    logout(req)
    return redirect('home')