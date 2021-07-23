from django.urls import path

from Textile_Market.textile_app.views import create_offer, page_401, edit_offer, \
    delete_offer, OffersView, HomePageView, MyOffersView, OfferDetailView

urlpatterns = [
    # path('', home_page, name='home'),
    path('', HomePageView.as_view(), name='home'),
    # path('offers', offers, name='offers'),
    path('offers', OffersView.as_view(), name='offers'),
    # path('my_offers/<int:pk>', my_offers, name='my offers'),
    path('my_offers/<int:pk>', MyOffersView.as_view(), name='my offers'),
    path('create/<int:pk>', create_offer, name='create offer'),
    # path('offer_details/<int:pk>', offer_details, name='details offer'),
    path('offer_details/<int:pk>', OfferDetailView.as_view(), name='details offer'),
    path('edit_offer/<int:pk>', edit_offer, name='edit offer'),
    path('delete_offer/<int:pk>', delete_offer, name='delete offer'),
    path('page_401', page_401, name='page 401'),
]