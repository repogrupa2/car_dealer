from django.db import models


# Create your models here.
class Branch(models.Model):
    address = models.CharField(max_length=39)
    city = models.CharField(max_length=16)
    mobile = models.SmallIntegerField("+48", max_length=11)
    opening_hours = models.TextField()
    mail = models.EmailField("e-mail address", max_length=39)
    remarks = models.TextField(null=True)

    def __str__(self):
        return f"Address {self.address} in {self.city} "
