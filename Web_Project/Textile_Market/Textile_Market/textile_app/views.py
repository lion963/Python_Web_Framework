from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from Textile_Market.textile_app.decorators import allowed_groups
from Textile_Market.textile_app.forms import OfferForm, ProfileForm, LoginForm
from Textile_Market.textile_app.models import AddOffer, Profile


def home_page(request):
    return render(request, 'home_page.html')


# def offers(request):
#     offers = AddOffer.objects.all()
#     context = {
#         'offers': offers
#     }
#     return render(request, 'offers.html', context)


class OffersView(ListView):
    context_object_name = 'offers'
    model = AddOffer
    template_name = 'offers.html'


def my_offers(request, pk):
    profile = Profile.objects.get(pk=pk)
    offers = AddOffer.objects.filter(profile_id=profile)
    context = {
        'offers': offers
    }
    return render(request, 'my_offers.html', context)


def offer_details(request, pk):
    condition = False
    offer = AddOffer.objects.get(pk=pk)
    if offer.profile.id == request.user.profile.id:
        condition = True
    context = {
        'offer': offer,
        'condition': condition
    }
    return render(request, 'offer_detail.html', context)


def edit_offer(request, pk):
    offer = AddOffer.objects.get(pk=pk)
    profile = Profile.objects.get(pk=offer.profile.id)
    if request.method == 'GET':
        form = OfferForm(instance=offer)
        return render(request, 'edit_offer.html', {'form': form})
    form = OfferForm(request.POST, request.FILES, instance=offer)
    if form.is_valid():
        offer = form.save(commit=False)
        offer.profile = profile
        offer.save()
        return redirect('details offer', pk=pk)
    return render(request, 'edit_offer.html', {'form': form})


def delete_offer(request, pk):
    offer = AddOffer.objects.get(pk=pk)
    if request.method == 'GET':
        form = OfferForm(instance=offer)
        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = True
            form.fields[field].widget.attrs['disabled'] = True
        return render(request, 'delete_offer.html', {'form': form, 'offer': offer})
    offer.delete()
    return redirect('my offers', pk=request.user.profile.id)


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

                    if len(Profile.objects.filter(user=user))==0:
                        profile = Profile(user=user, type='company', image='/static/assets/images/profile.jpg').save()
                        login(request, user)
                        return redirect('update')
                login(request, user)
                return redirect('home')
            else:
                context['wrong_credentials'] = True
                return render(request, 'login.html', context)
    return render(request, 'login.html', context)


@login_required(login_url='login')
@allowed_groups(['Company'])
def create_offer(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'GET':
        form = OfferForm()
        return render(request, 'create_offer.html', {'form':form})
    form = OfferForm(request.POST, request.FILES)
    if form.is_valid():
        offer = form.save(commit=False)
        offer.profile = profile
        offer.save()
        return redirect('offers')
    return render(request, 'create_offer.html', {'form':form})


def register(request):
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form
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
                if group.name == 'User' and profile.type=='person':
                    user.groups.add(group)
                if group.name == 'Company' and profile.type=='company':
                    user.groups.add(group)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            return redirect('login')
    return render(request, 'register.html', context)


def update_profile(request):
    user_form = UserCreationForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
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
                if group.name == 'User' and profile.type=='person':
                    user.groups.add(group)
                if group.name == 'Company' and profile.type=='company':
                    user.groups.add(group)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            return redirect('login')
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



def profile(request):
    if request.user.is_superuser:
        profiles = Profile.objects.all()
    else:
        profiles = [request.user.profile]
    context = {
        'profiles': profiles,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def page_401(request):
    return render(request, '401_page.html')