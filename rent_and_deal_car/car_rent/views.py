from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View

from .forms import BranchCreate
from .models import Branch


class ListOfBranches(View):
    def get(self, request, *args, **kwargs):
        list_of_branches = Branch.objects.all()
        ctx = {'list_of_branches': list_of_branches}
        return render(self.request, 'car_rent/list_of_branches.html', context=ctx)


class CreateBranch(View):
    def get(self, request, *args, **kwargs):
        form = BranchCreate()
        ctx = {'form': form}
        return render(self.request, "car_rent/create_branch.html", context=ctx)

    def post(self, request, *args, **kwargs):
        form = BranchCreate(data=request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.save()
            ctx = {'branch': branch, 'form': form}
            return render(self.request, "car_rent/create_branch.html", context=ctx)
        return render(self.request, "car_rent/list_of_branches.html", {'form': form})


class EditBranch(View):
    def get(self, request, branch_id, *args, **kwargs):
        try:
            branch = Branch.objects.get(id=branch_id)
        except Branch.DoesNotExist:
            ctx = {'branch_Id': id, 'errors': True}
            return render(self.request, "car_rent/create_branch.html", context=ctx)

        form = BranchCreate(instance=branch)
        ctx = {'branch': branch, 'form': form}
        return render(self.request, "car_rent/create_branch.html", context=ctx)

    def post(self, request, branch_id, *args, **kwargs):
        try:
            branch = Branch.objects.get(id=branch_id)
        except Branch.DoesNotExist:
            return HttpResponseBadRequest()
        form = BranchCreate(data=request.POST)
        if form.is_valid():
            branch.address = form.cleaned_data["address"]
            branch.city = form.cleaned_data["city"]
            branch.mobile = form.cleaned_data["mobile"]
            branch.open_from = form.cleaned_data["open_from"]
            branch.open_till = form.cleaned_data["open_till"]
            branch.mail = form.cleaned_data["mail"]
            branch.remarks = form.cleaned_data["remarks"]
            branch.save(update_fields=("address", "city", "mobile", "open_from", "open_till", "mail", "remarks"))

            ctx = {'form': form, 'branch': branch}
            return render(self.request, "car_rent/create_branch.html", context=ctx)

        ctx = {'errors': form.errors}
        return render(self.request, "car_rent/create_branch.html", context=ctx)


class BranchDelete(View):
    def get(self, request, branch_id, *args, **kwargs):
        try:
            branch = Branch.objects.get(id=branch_id)
        except Branch.DoesNotExist:
            ctx = {'branch_id': id, 'errors': True}
            return render(request, "car_rent/delete_branch.html", context=ctx)
        branch_id = branch.id
        branch.delete()

        ctx = {"is_deleted": True, "post": {"branch_id": branch_id}}

        return render(request, "car_rent/delete_branch.html", context=ctx)


class ViewBranch(View):
    def get(self, request, branch_id, *args, **kwargs):
        try:
            branch = Branch.objects.get(id=branch_id)
            ctx = {"branch": branch}
        except Branch.DoesNotExist:
            ctx = {'branch_id': id}
        return render(request, "car_rent/branch.html", context=ctx)
