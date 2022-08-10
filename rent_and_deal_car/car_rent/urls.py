
from django.urls import path

from .views import ListOfBranches, ViewBranch, CreateBranch, EditBranch, BranchDelete, VehicleList, AddVehicle, \
    UpdateVehicle, VehicleDelete, BrandList, \
    CreateBrand, CreateModel, ModelList

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
    path('createmodel/', CreateModel.as_view(), name="create-model")
    ]
    



