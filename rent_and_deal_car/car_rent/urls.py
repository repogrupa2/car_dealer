from django.conf.urls.static import static
from django.urls import path

from rent_and_deal_car import settings
from .views import ListOfBranches, ModelList,\
    ListOfRentalOffers, home, RentalOfferView, CarRentalDetails, ReturnCar,\
    AdminPanel, AccountDetails, CompleteDetails, AccountPayment

app_name = "car_rent"

urlpatterns = [
    path("", home, name="home"),
    path('admin/', AdminPanel.as_view(), name="switch-admin"),
    path('branches/', ListOfBranches.as_view(), name="list-of-branch"),
    path('listmodel/', ModelList.as_view(), name="list-model"),
    path('list_of_offers/', ListOfRentalOffers.as_view(), name="list-of-rental-offers"),
    path('offer/<int:RentalOffer_id>', RentalOfferView.as_view, name="rental-offer"),
    path('car_rental/<int:id>', CarRentalDetails.as_view(), name="car_rental"),
    path('car_rental_succesfull/', CarRentalDetails.as_view(), name="car_rental_succesfull"),
    path('car_rental_return/<int:id>', ReturnCar.as_view(), name="car_rental_return"),
    path('account_details/', AccountDetails.as_view(), name="account-details"),
    path('account-complete/', CompleteDetails.as_view(), name="account-complete"),
    path('account-payment/', AccountPayment.as_view(), name="account-payment"),
]
