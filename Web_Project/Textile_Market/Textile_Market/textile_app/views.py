from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')

def about_us(request):
    return render(request, 'about_us.html')

def offers(request):
    return render(request, 'offers.html')

def sign(request):
    return render(request, 'sign.html')