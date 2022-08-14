from django.conf.urls.static import static
from django.urls import path

from rent_and_deal_car import settings
from .views import ListOfBranches, ViewBranch, CreateBranch, EditBranch, BranchDelete, VehicleList, AddVehicle, \
    CreateOffer, UpdateVehicle, VehicleDelete, BrandList, \
    CreateBrand, CreateModel, ModelList, ListOfRentalOffers, home, aboutus, CarRental, RentalOfferView, RentalOfferEdit, \
    RentalOfferDelete, CarRentalDetails, account_details, AdminPanel

app_name = "car_rent"

urlpatterns = [

    path('branches/', ListOfBranches.as_view(), name="list-of-branch"),
    path('branch/<int:branch_id>', ViewBranch.as_view(), name="branch"),
    path('create_branch/', CreateBranch.as_view(), name="create-branch"),
    path('edit_branch/<int:branch_id>', EditBranch.as_view(), name="edit-branch"),
    path('delete_branch/<int:branch_id>', BranchDelete.as_view(), name="delete-branch"),
    path('vehiclelist/', VehicleList.as_view(), name="vehicle-list"),
    path('addvehicle/', AddVehicle.as_view(), name="add-vehicle"),
    path('updatevehicle/<int:vehicle_id>', UpdateVehicle.as_view(), name="update-vehicle"),
    path('deletevehicle/<int:vehicle_id>', VehicleDelete.as_view(), name="delete-vehicle"),
    path('listbrand/', BrandList.as_view(), name="list-brand"),
    path('createbrand/', CreateBrand.as_view(), name="create-brand"),
    path('listmodel/', ModelList.as_view(), name="list-model"),
    path('createmodel/', CreateModel.as_view(), name="create-model"),
    path('list_of_offers/', ListOfRentalOffers.as_view(), name="list-of-rental-offers"),
    path('offer/<int:RentalOffer_id>', RentalOfferView.as_view, name="rental-offer"),
    path('create_offer/', CreateOffer.as_view(), name="upload-offer"),
    path('edit/<int:RentalOffer_id>', RentalOfferEdit.as_view, name="edit-offer"),
    path('delete/<int:RentalOffer_id>', RentalOfferDelete.as_view, name="delete-offer"),
    path('car_rental/<int:id>',CarRentalDetails.as_view(), name="car_rental"),
    path('car_rental_succesfull/',CarRentalDetails.as_view(), name="car_rental_succesfull"),
    path('home/', home, name="home"),
    path('aboutus/', aboutus, name="aboutus"),
    path('account_details/', account_details, name="account-details"),
    path('admin/', AdminPanel.as_view(), name="switch-admin"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




