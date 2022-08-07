from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.forms import forms
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
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Brand(models.Model):
    name = models.CharField(max_length=16)


class BodyType(models.Model):
    name = models.CharField(max_length=16)


class Model(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
    name = models.CharField(max_length=16)


class Vehicle(models.Model):
    model_id = models.ForeignKey(Model, on_delete=models.PROTECT)
    body_type_id = models.ForeignKey(BodyType, on_delete=models.PROTECT)
    prod_year = models.IntegerField(max_length=4)
    color = models.CharField(max_length=16)
    engine = models.DecimalField(decimal_places=1, max_digits=2)
    type_of_fuel = models.CharField(max_length=16)
    transmission = models.CharField(max_length=16)
    mileage = models.DecimalField(decimal_places=1, max_digits=7)
    vin = models.IntegerField(max_length=17)
    photo = models.TextField(null=True)
    car_description = models.TextField(null=True)

    def __str__(self):
        return f"Model: {self.model_id}", f"Body: {self.body_type_id}", f"Production_Year: {self.prod_year}", \
               f"Color: {self.color}", f"Engine: {self.engine}", f"Type_of_Fuel: {self.type_of_fuel}", \
               f"Transmission_Id: {self.transmission}", f"Mileage: {self.mileage}", f"VIN: {self.vin}", \
               f"Photo: {self.photo}", f"Car_Description: {self.car_description}"


hours = [('00','00:00'),('01','01:00'),('02','02:00'),('03','03:00'),('04','04:00'),('05','05:00'),('06','06:00'),('07','07:00'),
         ('08','08:00'),('09','09:00'),('10','10:00'),('11','11:00'),('12','12:00'),('13','13:00'),('14','14:00'),('15','15:00'),
         ('16','16:00'),('17','17:00'),('18','18:00'),('19','19:00'),('20','20:00'),('21','21:00'),('22','22:00'),('23','23:00')]

class Branch(models.Model):
    address = models.CharField(max_length=39)
    city = models.CharField(max_length=16)
    phone_regex = RegexValidator(regex=r'(^[+]\d+(?:[ ]\d+)*)', message="Phone number must be entered in the format: '+00 000 000 000'. Up to 11 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17)
    open_from = models.CharField(max_length=6, choices=hours)
    open_till = models.CharField(max_length=6, choices=hours)
    mail = models.EmailField(max_length=39)
    remarks = models.TextField(null=True)

    def __str__(self):
        return f"Address: {self.address} in {self.city}, open from: {self.open_from}, open till: {self.open_till} ,mobile: {self.mobile}, " \
               f"mail {self.mail}"


class BranchCarAvailability(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.PROTECT)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    availability = models.BooleanField()

    def __str__(self):
        return f"Branch: {self.branch_id} , Car: {self.vehicle_id}, Availability: {self.availability}"


class RentalOffer(models.Model):
    Vehicle_Id = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    BranchCarAvailabilityId = models.ForeignKey(BranchCarAvailability, on_delete=models.PROTECT)
    Availability = models.CharField(null=True, max_length=4)
    Categories = models.CharField(max_length=16)
    Description = models.TextField(null=True)
    Deposit = models.DecimalField(decimal_places=2, max_digits=10)
    Price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Vehicle_Id: {self.Vehicle_Id}, {self.BranchCarAvailabilityId}, {self.Availability}," \
               f" {self.Categories}, {self.Description}, {self.Deposit}, {self.Price}"
