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

        fields = ('email', 'first_name', 'last_name',)


class BranchCreate(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('address', 'city', 'opening_hours', 'mail', 'mobile', 'remarks')


class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('model_id', 'body_type_id', 'prod_year', 'color', 'engine', 'type_of_fuel',
                  'transmission', 'mileage', 'vin', 'photo', 'car_description')
