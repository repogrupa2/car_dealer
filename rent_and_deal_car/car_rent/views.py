from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View

from .forms import BranchCreate, VehicleModelForm, BrandModelForm, CarModelModelForm, RentalOfferCreate
from .models import Branch, Vehicle, Brand, Model, RentalOffer


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


class ViewBranch(View):
    def get(self, request, branch_id, *args, **kwargs):
        try:
            branch = Branch.objects.get(id=branch_id)
            ctx = {"branch": branch}
        except Branch.DoesNotExist:
            ctx = {'branch_id': id}
        return render(request, "car_rent/branch.html", context=ctx)


def list_of_rental_offers(request):
    Offer = RentalOffer.objects.all()
    return render(request, 'car_rent/list_of_offers.html', {'offer': Offer})


def get_offer(request, RentalOffer_id):
    try:
        offer = RentalOffer.objects.get(id=RentalOffer_id)
    except RentalOffer.DoesNotExist:
        ctx = {'offer': offer}

    ctx = {'offer': offer}
    return render(request, "car_rent/offer.html", context=ctx)


def upload_offer(request):
    upload = RentalOfferCreate()
    if request.method == 'POST':
        upload = RentalOfferCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('list_of_offers')
        else:
            return HttpResponse()
    else:
        return render(request, 'car_rent/create_offer.html',{'create_offer':upload})


def update_RentalOffer(request, RentalOffer_id):
    RentalOffer_id = int(RentalOffer_id)
    try:
        RentalOffer_sel = RentalOffer.objects.get(id = RentalOffer_id)
    except RentalOffer.DoesNotExist:
        return redirect('list_of_offers')
    RentalOffer_form = RentalOfferCreate(request.POST or None, instance=RentalOffer_sel)
    if RentalOffer_form.is_valid():
       RentalOffer_form.save()
       return redirect('list_of_offers')
    return render(request, 'RentalOffer/upload_form.html', {'upload_form': RentalOffer_form})


def delete_RentalOffer(request, RentalOffer_id):
    RentalOffer_id = int(RentalOffer_id)
    try:
        RentalOffer_sel = RentalOffer.objects.get(id=RentalOffer_id)
    except RentalOffer.DoesNotExist:
        return redirect('list_of_offers')
    RentalOffer_sel.delete()
    return redirect('list_of_offers')


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

