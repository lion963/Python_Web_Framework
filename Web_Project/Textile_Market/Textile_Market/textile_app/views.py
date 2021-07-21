from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, TemplateView

from Textile_Market.textile_app.decorators import allowed_groups
from Textile_Market.textile_app.forms import OfferForm
from Textile_Market.textile_app.models import AddOffer
from Textile_Market.textile_profile.models import Profile

class HomePageView(TemplateView):
    template_name = 'common/home_page.html'

# def home_page(request):
#     return render(request, 'home_page.html')


@login_required(login_url='login')
@allowed_groups(['Company'])
def create_offer(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'GET':
        form = OfferForm()
        return render(request, 'app/create_offer.html', context={'form':form})
    form = OfferForm(request.POST, request.FILES)
    if form.is_valid():
        offer = form.save(commit=False)
        offer.profile = profile
        offer.save()
        return redirect('my offers', profile.id)
    return render(request, 'app/create_offer.html', context={'form':form})


class OffersView(ListView):
    context_object_name = 'offers'
    model = AddOffer
    template_name = 'common/offers.html'

# def offers(request):
#     offers = AddOffer.objects.all()
#     context = {
#         'offers': offers
#     }
#     return render(request, 'offers.html', context)

def my_offers(request, pk):
    profile = Profile.objects.get(pk=pk)
    offers = AddOffer.objects.filter(profile_id=profile)
    context = {
        'offers': offers
    }
    return render(request, 'app/my_offers.html', context)


def offer_details(request, pk):
    condition = False
    offer = AddOffer.objects.get(pk=pk)
    if offer.profile.id == request.user.profile.id or request.user.is_superuser:
        condition = True
    context = {
        'offer': offer,
        'condition': condition
    }
    return render(request, 'app/offer_detail.html', context)


def edit_offer(request, pk):
    offer = AddOffer.objects.get(pk=pk)
    profile = Profile.objects.get(pk=offer.profile.id)
    if request.method == 'GET':
        form = OfferForm(instance=offer)
        return render(request, 'app/edit_offer.html', {'form': form})
    form = OfferForm(request.POST, request.FILES, instance=offer)
    if form.is_valid():
        offer = form.save(commit=False)
        offer.profile = profile
        offer.save()
        return redirect('details offer', pk=pk)
    return render(request, 'app/edit_offer.html', {'form': form})


def delete_offer(request, pk):
    offer = AddOffer.objects.get(pk=pk)
    if request.method == 'GET':
        form = OfferForm(instance=offer)
        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = True
            form.fields[field].widget.attrs['disabled'] = True
        return render(request, 'app/delete_offer.html', {'form': form, 'offer': offer})
    offer.delete()
    return redirect('my offers', pk=request.user.profile.id)

def page_401(request):
    return render(request, 'common/401_page.html')
