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
