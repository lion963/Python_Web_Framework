from django.urls import path

from Textile_Market.textile_app.views import OffersView, HomePageView, MyOffersView, OfferDetailView, EditOfferView, DeleteOfferView, Page401View, \
    CreateOfferView

urlpatterns = [
    # path('', home_page, name='home'),
    path('', HomePageView.as_view(), name='home'),
    # path('offers', offers, name='offers'),
    path('offers', OffersView.as_view(), name='offers'),
    # path('my_offers/<int:pk>', my_offers, name='my offers'),
    path('my_offers/<int:pk>', MyOffersView.as_view(), name='my offers'),
    # path('create/<int:pk>', create_offer, name='create offer'),
    path('create/<int:pk>', CreateOfferView.as_view(), name='create offer'),
    # path('offer_details/<int:pk>', offer_details, name='details offer'),
    path('offer_details/<int:pk>', OfferDetailView.as_view(), name='details offer'),
    # path('edit_offer/<int:pk>', edit_offer, name='edit offer'),
    path('edit_offer/<int:pk>', EditOfferView.as_view(), name='edit offer'),
    # path('delete_offer/<int:pk>', delete_offer, name='delete offer'),
    path('delete_offer/<int:pk>', DeleteOfferView.as_view(), name='delete offer'),
    # path('page_401', page_401, name='page 401'),
    path('page_401', Page401View.as_view(), name='page 401'),
]