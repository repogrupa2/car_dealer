from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
# służy do internacjonalizacji I18N
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(blank=True, max_length=30, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=30, verbose_name='last name')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class RentalOffer(models.Model):
    Vehicle_Id = models.ForeignKey(Vehicle)
    Branch_Id_Availability = models.ForeignKey(Branch)
    Availability = models.CharField(null=True, max_length=4)
    Categories = models.CharField(max_length=16)
    Description = models.TextField(null=True)
    Deposit = models.DecimalField(2)
    Price = models.DecimalField(2)

    def __str__(self):
        return f"Vehicle_Id: {self.Vehicle_Id}, {self.Branch_Id_Availability}, {self.Availability}, {self.Categories}, {self.Description}, {self.Deposit}, {self.Price}"


class Brand(models.Model):
    name = models.CharField(max_length=16)


class BodyType(models.Model):
    name = models.CharField(max_length=16)


class Model(models.Model):
    brand_id = models.ForeignKey(Brand)
    name = models.CharField(max_length=16)


class Vehicle(models.Model):
    model_id = models.ForeignKey(Model)
    body_type_id = models.ForeignKey(BodyType)
    prod_year = models.SmallIntegerField(max_length=4)
    color = models.CharField(max_length=16)
    engine = models.DecimalField(decimal_places=1, max_digits=2)
    type_of_fuel = models.CharField(max_length=16)
    transmission = models.CharField(max_length=16)
    mileage = models.DecimalField(decimal_places=1, max_digits=7)
    vin = models.SmallIntegerField(max_length=17)
    photo = models.TextField(null=True)
    car_description = models.TextField(null=True)

    def __str__(self) -> [tuple]:
        return f"Model: {self.model_id}", f"Body: {self.body_type_id}", f"Production_Year: {self.prod_year}", \
                        f"Color: {self.color}", f"Engine: {self.engine}", f"Type_of_Fuel: {self.type_of_fuel}", \
               f"Transmission_Id: {self.transmission}", f"Mileage: {self.mileage}", f"VIN: {self.vin}", \
               f"Photo: {self.photo}", f"Car_Description: {self.car_description}"
               

class Branch(models.Model):
    address = models.CharField(max_length=39)
    city = models.CharField(max_length=16)
    mobile = models.CharField(max_length=15)
    opening_hours = models.TextField()
    mail = models.EmailField(max_length=39)
    remarks = models.TextField(null=True)

    def __str__(self):
        return f"Address {self.address} in {self.city}, opening hours {self.opening_hours}, mobile {self.mobile}, " \
               f"mail {self.mail} "
