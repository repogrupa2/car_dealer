from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.
User = AUTH_USER_MODEL


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
