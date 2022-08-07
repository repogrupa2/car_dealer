from django.urls import path
from . import views
from .views import ViewBranch, CreateBranch, EditBranch, BranchDelete, ListOfBranches

app_name = "car_rent"

urlpatterns = [
    path('branches/', ListOfBranches.as_view(),name = "list-of-branch"),
    path('branch/<int:branch_id>', ViewBranch.as_view(), name = "branch"),
    path('create_branch/',CreateBranch.as_view(),name = "create-branch"),
    path('edit_branch/<int:branch_id>', EditBranch.as_view(),name = "edit-branch"),
    path('delete_branch/<int:branch_id>', BranchDelete.as_view(),name = "delete-branch"),
    ]