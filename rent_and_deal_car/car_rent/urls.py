from django.urls import path
from .views import list_of_branch, get_branch, create_branch, edit_branch, delete_branch, list_of_rental_offers, \
    upload_offer, get_offer, update_RentalOffer, delete_RentalOffer

app_name = "car_rent"

urlpatterns = [
    path('branches/', list_of_branch,name = "list-of-branch"),
    path('branch/<int:branch_id>', get_branch, name = "branch"),
    path('create_branch/', create_branch,name = "create-branch"),
    path('edit/<int:branch_id>', edit_branch,name = "edit-branch"),
    path('delete/<int:branch_id>', delete_branch,name = "delete-branch"),

    path('list_of_offers/', list_of_rental_offers, name = "list-of-rental-offers"),
    path('offer/<int:RentalOffer_id>', get_offer, name="rental-offer"),
    path('create_offer/', upload_offer, name = "upload-offer"),
    path('edit/<int:RentalOffer_id>', update_RentalOffer,name = "edit-offer"),
    path('delete/<int:RentalOffer_id>', delete_RentalOffer,name = "delete-offer"),
    ]