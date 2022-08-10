from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View
from .forms import BranchCreate, VehicleModelForm, BrandModelForm, CarModelModelForm, RentalOfferCreate, CustomerCreate 
from .models import Branch, Vehicle, Brand, Model, RentalOffer, CarRental, BranchCarAvailability, Customer
import datetime


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


class ListOfRentalOffers(View):
    def get(self, request, *args, **kwargs):
        list_of_offers = RentalOffer.objects.all()
        ctx = {'list_of_offers': list_of_offers}
        return render(self.request, 'car_rent/list_of_offers.html', context=ctx)


class CreateOffer(View):
    def get(self, request, *args, **kwargs):
        form = RentalOfferCreate()
        ctx = {'form': form}
        return render(self.request, "car_rent/create_offer.html", context=ctx)

    def post(self, request, *args, **kwargs):
        form = RentalOfferCreate(data=request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.save()
            ctx = {'offer': offer, 'form': form}
            return render(self.request, "car_rent/create_offer.html", context=ctx)
        return render(self.request, "car_rent/list_of_offers.html", {'form': form})


class RentalOfferEdit(View):
    def get(self, request, rental_offer_id, *args, **kwargs):
        try:
            rental_offer = RentalOffer.objects.get(id=rental_offer_id)
        except RentalOffer.DoesNotExist:
            ctx = {'rental_offer_id': id, 'errors': True}
            return render(self.request, "car_rent/create_offer.html", context=ctx)
            
        form = RentalOfferCreate(instance=rental_offer)
        ctx = {'rental_offer': rental_offer, 'form': form}
        return render(self.request, "car_rent/create_offer.html", context=ctx)

    def post(self, request, rental_offer_id, *args, **kwargs):
        try:
            rental_offer = RentalOffer.objects.get(id=rental_offer_id)
        except RentalOffer.DoesNotExist:
            return HttpResponseBadRequest()
        form = RentalOfferCreate(data=request.POST)
        if form.is_valid():
            rental_offer.vehicle_Id = form.cleaned_data["vehicle_Id"]
            rental_offer.branchCarAvailability_Id = form.cleaned_data["branchCarAvailability_Id"]
            rental_offer.categories = form.cleaned_data["categories"]
            rental_offer.description = form.cleaned_data["description"]
            rental_offer.deposit = form.cleaned_data["deposit"]
            rental_offer.price_per_day = form.cleaned_data["price_per_day"]
            rental_offer.save(update_fields=("vehicle_Id", "branchCarAvailability_Id", "categories", "description",
            "deposit", "price_per_day"))

            ctx = {'form': form, 'rental_offer': rental_offer}
            return render(self.request, "car_rent/create_offer.html", context=ctx)

        ctx = {'errors': form.errors}
        return render(self.request, "car_rent/create_offer.html", context=ctx)


class RentalOfferDelete(View):
    def get(self, request, rental_offer_id, *args, **kwargs):
        try:
            rental_offer = RentalOffer.objects.get(id=rental_offer_id)
        except RentalOffer.DoesNotExist:
            ctx = {'rental_offer_id': id, 'errors': True}
            return render(request, "car_rent/delete_offer.html", context=ctx)
        rental_offer_id = rental_offer.id
        rental_offer.delete()


class RentalOfferView(View):
    def get(self, request, rental_offer_id, *args, **kwargs):
        try:
            rental_offer = RentalOffer.objects.get(id=rental_offer_id)
            ctx = {"rental_offer": rental_offer}
        except RentalOffer.DoesNotExist:
            ctx = {'rental_offer_id': id}
        return render(request, "car_rent/offer.html", context=ctx)


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
    def get(self, request, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(id=1)
        except Vehicle.DoesNotExist:
            ctx = {'Vehicle_Id': id, 'errors': True}
            return render(request, "car_rent/updatevehicle.html", context=ctx)

        form = VehicleModelForm(instance=vehicle)
        ctx = {'vehicle': vehicle, 'form': form}
        return render(request, "car_rent/updatevehicle.html", context=ctx)

    def post(self, request, *args, **kwargs):
        try:
            vehicle = Vehicle.objects.get(id=1)
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
            return render(request, "car_rent/updatevehicle.html", context=ctx)

        ctx = {'errors': form.errors}
        return render(request, "car_rent/updatevehicle.html", context=ctx)


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


def home(request):
    return render(request, "car_rent/home.html")

def aboutus(request):
    return render(request, "car_rent/about_us.html")


class CarRental(View):
    def get(self, request, id, *args, **kwargs):
        try:
            rental = CarRental.objects.get(id=id)
            ctx = {"rental": rental}
        except:
            ctx = {'id': id}

        return render(request, "car_rent/car_rental.html", context=ctx)


class ListOfCustomers(View):
  def get(self, request, *args, **kwargs):
        list_of_customers = Customer.objects.all()
        ctx = {'list_of_customers': list_of_customers}
        return render(self.request, 'car_rent/list_of_customers.html', context=ctx)


class CustomerCreate(View):
    def get(self, request, *args, **kwargs):
        form = CustomerCreate()
        ctx = {'form': form}
        return render(self.request, "car_rent/customer_create.html", context=ctx)

    def post(self, request, *args, **kwargs):
        form = CustomerCreate(data=request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            ctx = {'customer': customer, 'form': form}
            return render(self.request, "car_rent/customer_create.html", context=ctx)
        return render(self.request, "car_rent/customer_create.html", {'form': form})


class CustomerEdit(View):
    def get(self, request, customer_id, *args, **kwargs):
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            ctx = {'customer_id': id, 'errors': True}
            return render(self.request, "car_rent/customer_create.html", context=ctx)

        form = CustomerCreate(instance=customer)
        ctx = {'customer': customer, 'form': form}
        return render(self.request, "car_rent/customer_create.html", context=ctx)

    def post(self, request, customer_id, *args, **kwargs):
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return HttpResponseBadRequest()
        form = CustomerCreate(data=request.POST)
        if form.is_valid():
            customer.name = form.cleaned_data["name"]
            customer.surname = form.cleaned_data["surname"]
            customer.address = form.cleaned_data["address"]
            customer.company = form.cleaned_data["company"]
            customer.credit_card_nr = form.cleaned_data["credit_card_nr"]
            customer.tax_id = form.cleaned_data["tax_id"]
            customer.mobile = form.cleaned_data["mobile"]
            customer.email = form.cleaned_data["email"]
            customer.save(update_fields=("name", "surname", "address", "company", "credit_card_nr", "tax_id", "mobile",
            "email"))

            ctx = {'form': form, 'customer': customer}
            return render(self.request, "car_rent/customer_create.html", context=ctx)

        ctx = {'errors': form.errors}
        return render(self.request, "car_rent/customer_create.html", context=ctx)


class CustomerDelete(View):
    def get(self, request, customer_id, *args, **kwargs):
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            ctx = {'customer_id': id, 'errors': True}
            return render(request, "car_rent/customer_delete.html", context=ctx)
        customer_id = customer.id
        customer.delete()


class CustomerView(View):
    def get(self, request, customer_id, *args, **kwargs):
        try:
            customer = Customer.objects.get(id=customer_id)
            ctx = {"customer": customer}
        except Customer.DoesNotExist:
            ctx = {'customer_id': id}
        return render(request, "car_rent/customer.html", context=ctx)

