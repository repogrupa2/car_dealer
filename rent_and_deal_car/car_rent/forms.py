from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Vehicle, Branch, Brand, Model, RentalOffer, CarRental


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)


class CustomUserCompleteDetails(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('street', 'house_number', 'zip_code',
                  'city', 'credit_card_nr', 'expiration',
                  'CVV', 'mobile')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('credit_card_nr', 'balance',  'password',)


class BranchCreate(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('address', 'city', 'open_from', 'open_till',
                  'mail', 'mobile', 'remarks')


class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('model_id', 'body_type', 'prod_year',
                  'color', 'engine', 'type_of_fuel',
                  'transmission', 'vin')


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name',)


class CarModelModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ('brand_id', 'name',)


class RentalOfferCreate(forms.ModelForm):
    class Meta:
        model = RentalOffer
        fields = ('Vehicle_Id', 'Categories',
                  'Description', 'Deposit', 'Price_per_day')


class CarRentalForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = ('customer_id', 'rental_offer_id', 'total_price')
