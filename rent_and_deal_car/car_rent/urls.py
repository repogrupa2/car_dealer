from django.conf.urls.static import static
from django.urls import path

from rent_and_deal_car import settings
from .views import ListOfBranches, ViewBranch, VehicleList, \
    BrandList, \
    ModelList, ListOfRentalOffers, home, aboutus, RentalOfferView, \
    CarRentalDetails, ReturnCar, AdminPanel, AccountDetails, CompleteDetails, AccountPayment

app_name = "car_rent"

urlpatterns = [
    path("", home, name="home"),
    path('"admin/', AdminPanel.as_view(), name="switch-admin"),
    path('aboutus/', aboutus, name="aboutus"),
    path('branches/', ListOfBranches.as_view(), name="list-of-branch"),
    path('branch/<int:branch_id>', ViewBranch.as_view(), name="branch"),
    path('vehiclelist/', VehicleList.as_view(), name="vehicle-list"),
    path('listbrand/', BrandList.as_view(), name="list-brand"),
    path('listmodel/', ModelList.as_view(), name="list-model"),
    path('list_of_offers/', ListOfRentalOffers.as_view(), name="list-of-rental-offers"),
    path('offer/<int:RentalOffer_id>', RentalOfferView.as_view, name="rental-offer"),
    path('car_rental/<int:id>', CarRentalDetails.as_view(), name="car_rental"),
    path('car_rental_succesfull/', CarRentalDetails.as_view(), name="car_rental_succesfull"),
    path('car_rental_return/<int:id>', ReturnCar.as_view(), name="car_rental_return"),
    path('account_details/', AccountDetails.as_view(), name="account-details"),
    path('account-complete/', CompleteDetails.as_view(), name="account-complete"),
    path('account-payment/', AccountPayment.as_view(), name="account-payment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
