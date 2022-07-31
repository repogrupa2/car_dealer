from django.db import models


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
