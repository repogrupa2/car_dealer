from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views import View


from .models import CustomUser, Vehicle, Branch
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser

        fields = ('email', 'first_name', 'last_name', )


class VehicleList(View):
    def get(self, request, *args, **kwargs):
        vehicles = Vehicle.objects.all()
        ctx = {'vehicles': vehicles}
        return render(self.request, "car_rent/vehicles.html", context=ctx)

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
            return render(self.request, "car_rent/addvehicle.html",context=ctx)
        return render(self.request, "car_rent/addvehicle.html", {'form': form})

class UpdateVehicle(View):
    def get(self, request, id, *args, **kwargs):
        try:
            vehicle= Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            ctx = {'Vehicle_Id': id, 'errors': True}
            return render(self.request, "car_rent/updatevehicle.html",context=ctx)

        form = VehicleModelForm(instance=vehicle)
        ctx = {'vehicle': vehicle, 'form': form}
        return render(self.request, "car_rent/updatevehicle.html", context=ctx)

    def post(self, request, id, *args, **kwargs):
        try:
            vehicle= Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            return HttpResponseBadRequest()
        form = VehicleModelForm(data=request.POST)
        if form.is_valid():
            vehicle.model_id = form.cleaned_data["Model_id"]
            vehicle.body_type_id = form.cleaned_data["BodyType"]
            vehicle.prod_year = form.cleaned_data["ProductionYear"]
            vehicle.color = form.cleaned_data["Color"]
            vehicle.engine = form.cleaned_data["Engine"]
            vehicle.type_of_fuel = form.cleaned_data["TypeOfFuel"]
            vehicle.transmission = form.cleaned_data["Transmission"]
            vehicle.mileage = form.cleaned_data["Mileage"]
            vehicle.vin = form.cleaned_data["VIN"]
            vehicle.photo = form.cleaned_data["Photo"]
            vehicle.car_description = form.cleaned_data["CarDescription"]
            vehicle.save(update_fields=('Model_id', 'BodyType', 'ProductionYear', 'Color', 'Engine', 'TypeOfFuel'
                                        'Transmission', 'Mileage', 'VIN', 'Photo', 'CarDescription'))

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

        fields = ('email', 'first_name', 'last_name',)


class BranchCreate(forms.ModelForm):

    class Meta:
        model = Branch
        fields = ('address', 'city', 'opening_hours', 'mail','mobile', 'remarks')

