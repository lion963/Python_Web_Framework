from django.shortcuts import render, redirect

from Textile_Market.textile_app.forms import AddOfferForm
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

def sign(request):
    return render(request, 'sign.html')

def create_offer(request):
    if request.method == 'GET':
        form = AddOfferForm()
        return render(request, 'create_offer.html', {'form':form})
    form = AddOfferForm(request.POST, request.FILES)
    if form.is_valid():
        offer = form.save()
        offer.save()
        return redirect('offers')
    return render(request, 'create_offer.html', {'form':form})

def offer_details(request):
    return render(request, 'offer_detail.html')