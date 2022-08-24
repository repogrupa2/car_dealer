from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
# It is used for internationalization I18N
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from car_rent.regex import phone_regex


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(blank=True, max_length=30, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=30, verbose_name='last name')
    street = models.CharField(max_length=39, null=True)
    house_number = models.CharField(max_length=8, null=True)
    zip_code = models.CharField(max_length=8, null=True)
    city = models.CharField(max_length=16, null=True)
    credit_card_nr = models.CharField(max_length=39, null=True)
    expiration = models.CharField(max_length=8, null=True)
    CVV = models.CharField(max_length=4, null=True)
    mobile = models.CharField(validators=[phone_regex], max_length=17)
    balance = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Brand(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Model(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
    name = models.CharField(max_length=16)

    def __str__(self):
        return f" {self.brand_id} {self.name}"


gearbox = [('Automatic', 'Automatic'), ('Manual', 'Manual')]

fuel = [('Diesel', 'Diesel'), ('Gasoline', 'Gasoline'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')]

body = [('Sedan', 'Sedan'), ('Combi', 'Combi'), ('SUV', 'SUV'), ('Sport', 'Sport')]


class Vehicle(models.Model):
    model_id = models.ForeignKey(Model, on_delete=models.PROTECT)
    body_type = models.CharField(max_length=16, choices=body)
    prod_year = models.CharField(max_length=4)
    color = models.CharField(max_length=16)
    engine = models.DecimalField(decimal_places=1, max_digits=2)
    type_of_fuel = models.CharField(max_length=16, choices=fuel)
    transmission = models.CharField(max_length=16, choices=gearbox)
    vin = models.CharField(max_length=17, unique=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"Model: {self.model_id}"


open_hours = [('05', '05:00'), ('06', '06:00'), ('07', '07:00'), ('08', '08:00'),
              ('09', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00')]

close_hours = [('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'),
               ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'),
               ('21', '21:00'), ('22', '22:00'), ('23', '23:00')]


class Branch(models.Model):
    address = models.CharField(max_length=39)
    city = models.CharField(max_length=16)
    mobile = models.CharField(validators=[phone_regex], max_length=17)
    open_from = models.CharField(max_length=6, choices=open_hours)
    open_till = models.CharField(max_length=6, choices=close_hours)
    mail = models.EmailField(max_length=39)
    remarks = models.TextField(null=True)

    def __str__(self):
        return f"Address: {self.address} in {self.city}, open from: {self.open_from}," \
               f" open till: {self.open_till} ,mobile: {self.mobile}, mail: {self.mail}"


categories = [('Economy', 'Economy'), ('Intermediate ', 'Intermediate '), ('Premium', 'Premium'), ('Luxury', 'Luxury')]


class RentalOffer(models.Model):
    Vehicle_Id = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    Categories = models.CharField(max_length=13, choices=categories)
    Description = models.TextField(null=True)
    Deposit = models.DecimalField(decimal_places=2, max_digits=10)
    Price_per_day = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Vehicle_Id: {self.Vehicle_Id}"


class CarRental(models.Model):
    customer_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    rental_offer_id = models.ForeignKey(RentalOffer, on_delete=models.PROTECT)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    date_of_rent = models.DateField(auto_now_add=True)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return f"Customer ID: {self.customer_id}, and rental offer {self.rental_offer_id}"
