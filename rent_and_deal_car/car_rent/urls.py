from django.urls import path
from .views import list_of_branch, get_branch, create_branch, edit_branch, delete_branch, ListOfRentalOffer

app_name = "car_rent"

urlpatterns = [
    path('branches/', list_of_branch,name = "list-of-branch"),
    path('branch/<int:branch_id>', get_branch, name = "branch"),
    path('create_branch/', create_branch,name = "create-branch"),
    path('edit/<int:branch_id>', edit_branch,name = "edit-branch"),
    path('delete/<int:branch_id>', delete_branch,name = "delete-branch"),
    path('list_of_offers/', ListOfRentalOffer),
    ]