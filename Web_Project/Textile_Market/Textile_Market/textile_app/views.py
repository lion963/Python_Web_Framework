from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView, CreateView

from Textile_Market.textile_app.decorators import allowed_groups
from Textile_Market.textile_app.forms import OfferForm
from Textile_Market.textile_app.mixins import GroupRequiredMixin
from Textile_Market.textile_app.models import AddOffer
from Textile_Market.textile_profile.models import Profile


class HomePageView(TemplateView):
    template_name = 'common/home_page.html'


class CreateOfferView(GroupRequiredMixin, CreateView):
    template_name = 'app/create_offer.html'
    model = AddOffer
    form_class = OfferForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.profile = self.request.user.profile
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my offers', kwargs={'pk': self.request.user.profile.id})


class OffersView(ListView):
    context_object_name = 'offers'
    model = AddOffer
    template_name = 'common/offers.html'


class MyOffersView(ListView):
    model = AddOffer
    template_name = 'app/my_offers.html'
    context_object_name = 'offers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = context['offers'].filter(profile_id=self.request.user.profile)
        return context


class OfferDetailView(DetailView):
    model = AddOffer
    template_name = 'app/offer_detail.html'
    context_object_name = 'offer'

    def get_context_data(self, **kwargs):
        condition = False
        if self.object.profile.id == self.request.user.profile.id or self.request.user.is_superuser:
            condition = True
        context = super().get_context_data(**kwargs)
        context['condition'] = condition
        return context


class EditOfferView(UpdateView):
    template_name = 'app/edit_offer.html'
    model = AddOffer
    form_class = OfferForm

    def get_success_url(self):
        return reverse_lazy('details offer', kwargs={'pk': self.object.pk})


class DeleteOfferView(DeleteView):
    template_name = 'app/delete_offer.html'
    model = AddOffer
    form_class = OfferForm
    context_object_name = 'offer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(instance=context['offer'])
        for field in form.fields:
            form.fields[field].widget.attrs['readonly'] = True
            form.fields[field].widget.attrs['disabled'] = True
        context['form'] = form
        return context

    def get_success_url(self):
        return reverse_lazy('my offers', kwargs={'pk': self.request.user.profile.id})


class Page401View(TemplateView):
    template_name = 'common/401_page.html'


# def home_page(request):
#     return render(request, 'home_page.html')


# @login_required(login_url='login')
# @allowed_groups(['Company'])
# def create_offer(request, pk):
#     profile = Profile.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = OfferForm()
#         return render(request, 'app/create_offer.html', context={'form':form})
#     form = OfferForm(request.POST, request.FILES)
#     if form.is_valid():
#         offer = form.save(commit=False)
#         offer.profile = profile
#         offer.save()
#         return redirect('my offers', profile.id)
#     return render(request, 'app/create_offer.html', context={'form':form})


# def offers(request):
#     offers = AddOffer.objects.all()
#     context = {
#         'offers': offers
#     }
#     return render(request, 'offers.html', context)

# def my_offers(request, pk):
#     profile = Profile.objects.get(pk=pk)
#     offers = AddOffer.objects.filter(profile_id=profile)
#     context = {
#         'offers': offers
#     }
#     return render(request, 'app/my_offers.html', context)

# def offer_details(request, pk):
#     condition = False
#     offer = AddOffer.objects.get(pk=pk)
#     if offer.profile.id == request.user.profile.id or request.user.is_superuser:
#         condition = True
#     context = {
#         'offer': offer,
#         'condition': condition
#     }
#     return render(request, 'app/offer_detail.html', context)

# def edit_offer(request, pk):
#     offer = AddOffer.objects.get(pk=pk)
#     profile = Profile.objects.get(pk=offer.profile.id)
#     if request.method == 'GET':
#         form = OfferForm(instance=offer)
#         return render(request, 'app/edit_offer.html', {'form': form})
#     form = OfferForm(request.POST, request.FILES, instance=offer)
#     if form.is_valid():
#         offer = form.save(commit=False)
#         offer.profile = profile
#         offer.save()
#         return redirect('details offer', pk=pk)
#     return render(request, 'app/edit_offer.html', {'form': form})

# def delete_offer(request, pk):
#     offer = AddOffer.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = OfferForm(instance=offer)
#         for field in form.fields:
#             form.fields[field].widget.attrs['readonly'] = True
#             form.fields[field].widget.attrs['disabled'] = True
#         return render(request, 'app/delete_offer.html', {'form': form, 'offer': offer})
#     offer.delete()
#     return redirect('my offers', pk=request.user.profile.id)

# def page_401(request):
#     return render(request, 'common/401_page.html')
