from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View

from .forms import BranchCreate, VehicleModelForm, BrandModelForm, CarModelModelForm
from .models import Branch, Vehicle, Brand, Model


def list_of_branch(request):
    list_of_branches = Branch.objects.all()
    return render(request, 'car_rent/list_of_branches.html', {'list_of_branches': list_of_branches})


def create_branch(request):
    form = BranchCreate()
    if request.method == 'POST':
        form = BranchCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_rent:list-of-branch')

    ctx = {'form': form}
    return render(request, 'car_rent/create_branch.html', ctx)


def edit_branch(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    form = BranchCreate(instance=branch)
    if request.method == 'POST':
        form = BranchCreate(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('car_rent:list-of-branch')

    ctx = {'form': form}
    return render(request, 'car_rent/create_branch.html', ctx)


def delete_branch(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    if request.method == 'POST':
        branch.delete()
        return redirect('car_rent:list-of-branch')

    ctx = {'item': branch}
    return render(request, 'car_rent/delete_branch.html', ctx)


def get_branch(request, branch_id):
    try:
        branch = Branch.objects.get(id=branch_id)
    except Branch.DoesNotExist:
        ctx = {'branch': branch}

    ctx = {'branch': branch}
    return render(request, "car_rent/branch.html", context=ctx)


class VehicleList(View):
    def get(self, request, *args, **kwargs):
        vehicles = Vehicle.objects.all()
        ctx = {'vehicles': vehicles}
        return render(self.request, "car_rent/vehiclelist.html", context=ctx)


class AddVehicle(View):
    def get(self, request, *args, **kwargs):
        form = VehicleModelForm()
        ctx = {'form': form}
        return render(self.request, "car_rent/addvehicle.html", context=ctx)

    def post(self, request, *args, **kwargs):
        form = VehicleModelForm(data=request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.save()
            ctx = {'vehicle': vehicle, 'form': form}
            return render(self.request, "car_rent/addvehicle.html", context=ctx)
        return render(self.request, "car_rent/addvehicle.html", {'form': form})


class UpdateVehicle(View):
    def get(self, request, id, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            ctx = {'Vehicle_Id': id, 'errors': True}
            return render(self.request, "car_rent/updatevehicle.html", context=ctx)

        form = VehicleModelForm(instance=vehicle)
        ctx = {'vehicle': vehicle, 'form': form}
        return render(self.request, "car_rent/updatevehicle.html", context=ctx)

    def post(self, request, id, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            return HttpResponseBadRequest()
        form = VehicleModelForm(data=request.POST)
        if form.is_valid():
            vehicle.model_id = form.cleaned_data["Model_id"]
            vehicle.body_type = form.cleaned_data["BodyType"]
            vehicle.prod_year = form.cleaned_data["ProductionYear"]
            vehicle.color = form.cleaned_data["Color"]
            vehicle.engine = form.cleaned_data["Engine"]
            vehicle.type_of_fuel = form.cleaned_data["TypeOfFuel"]
            vehicle.transmission = form.cleaned_data["Transmission"]
            vehicle.vin = form.cleaned_data["VIN"]
            vehicle.photo = form.cleaned_data["Photo"]
            vehicle.save(update_fields=('Model_id', 'BodyType', 'ProductionYear', 'Color', 'Engine', 'TypeOfFuel'
                                                                                                     'Transmission',
                                         'VIN', 'Photo'))


            ctx = {'form': form, 'vehicle': vehicle}
            return render(self.request, "car_rent/updatevehicle.html", context=ctx)

        ctx = {'errors': form.errors}
        return render(self.request, "car_rent/updatevehicle.html", context=ctx)


class VehicleDelete(View):
    def get(self, request, id, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            ctx = {'vehicle_id': id, 'errors': True}
            return render(request, "car_rent/vehicle_delete.html", context=ctx)
        vehicle_model = vehicle.model
        vehicle_id = vehicle.id
        vehicle.delete()

        ctx = {"is_deleted": True, "post": {"vehicle_model": vehicle_model, "vehicle_id": vehicle_id}}

        return render(request, "car_rent/vehicle_delete.html", context=ctx)


class CreateBrand(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = BrandModelForm()
        ctx = {'form': form}
        return render(self.request, "car_rent/create_brand.html", context=ctx)

    def post(self, request, *args, **kwargs):
        form = BrandModelForm(data=request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            ctx = {'brand': brand, 'form': form}

            return render(self.request, "car_rent/create_brand.html", context=ctx)
            
        return render(self.request, "car_rent/create_brand.html", {'form': form})

class BrandList(View):
    def get(self, request, *args, **kwargs):
        brand = Brand.objects.all()
        ctx = {'brand': brand}
        
        return render(self.request, "car_rent/brand_list.html", context=ctx)


class CreateModel(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = CarModelModelForm()
        ctx = {'form': form}
        
        return render(self.request, "car_rent/create_model.html", context=ctx)

    def post(self, request, *args, **kwargs):
        form = CarModelModelForm(data=request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            ctx = {'model': model, 'form': form}
            return render(self.request, "car_rent/create_model.html", context=ctx)
            
        return render(self.request, "car_rent/create_model.html", {'form': form})


class ModelList(View):
    def get(self, request, *args, **kwargs):
        model = Model.objects.all()
        ctx = {'model': model}
        
        return render(self.request, "car_rent/model_list.html", context=ctx)