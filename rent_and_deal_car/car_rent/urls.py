
from django.urls import path
from . import views
from .views import list_of_branch, get_branch, create_branch, edit_branch, delete_branch, VehicleList, AddVehicle, \
    UpdateVehicle, VehicleDelete, BrandList, CreateBrand, CreateModel, ModelList

app_name = "car_rent"

urlpatterns = [
    path('branches/', list_of_branch, name="list-of-branch"),
    path('branch/<int:branch_id>', get_branch, name="branch"),
    path('create_branch/', create_branch, name="create-branch"),
    path('edit/<int:branch_id>', edit_branch, name="edit-branch"),
    path('delete/<int:branch_id>', delete_branch, name="delete-branch"),
    path('vehiclelist/', VehicleList.as_view(), name="vehicle-list"),
    path('addvehicle/', AddVehicle.as_view(), name="add-vehicle"),
    path('updatevehicle/<int:vehicle_id>', UpdateVehicle.as_view(), name="update-vehicle"),
    path('deletevehicle/<int:vehicle_id>', VehicleDelete.as_view(), name="delete-vehicle"),

    path('listbrand/', BrandList.as_view(), name="list-brand"),
    path('createbrand/', CreateBrand.as_view(), name="create-brand"),

    path('listmodel/', ModelList.as_view(), name="list-model"),
    path('createmodel/', CreateModel.as_view(), name="create-model"),
    ]
