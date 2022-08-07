
from django.urls import path

from .views import ListOfBranches, ViewBranch, CreateBranch, EditBranch, BranchDelete, VehicleList, AddVehicle, \
    upload_offer, get_offer, update_RentalOffer, delete_RentalOffer, UpdateVehicle, VehicleDelete, BrandList, CreateBrand, CreateModel, ModelList


app_name = "car_rent"

urlpatterns = [

    path('branches/', ListOfBranches.as_view(),name = "list-of-branch"),
    path('branch/<int:branch_id>', ViewBranch.as_view(), name = "branch"),
    path('create_branch/',CreateBranch.as_view(),name = "create-branch"),
    path('edit_branch/<int:branch_id>', EditBranch.as_view(),name = "edit-branch"),
    path('delete_branch/<int:branch_id>', BranchDelete.as_view(),name = "delete-branch"),
    
    path('vehiclelist/', VehicleList.as_view(), name="vehicle-list"),
    path('addvehicle/', AddVehicle.as_view(), name="add-vehicle"),
    path('updatevehicle/<int:vehicle_id>', UpdateVehicle.as_view(), name="update-vehicle"),
    path('deletevehicle/<int:vehicle_id>', VehicleDelete.as_view(), name="delete-vehicle"),

    path('listbrand/', BrandList.as_view(), name="list-brand"),
    path('createbrand/', CreateBrand.as_view(), name="create-brand"),

    path('listmodel/', ModelList.as_view(), name="list-model"),
    path('createmodel/', CreateModel.as_view(), name="create-model"),
    
    path('list_of_offers/', list_of_rental_offers, name = "list-of-rental-offers"),
    path('offer/<int:RentalOffer_id>', get_offer, name="rental-offer"),
    path('create_offer/', upload_offer, name = "upload-offer"),
    path('edit/<int:RentalOffer_id>', update_RentalOffer,name = "edit-offer"),
    path('delete/<int:RentalOffer_id>', delete_RentalOffer,name = "delete-offer"),
    ]


