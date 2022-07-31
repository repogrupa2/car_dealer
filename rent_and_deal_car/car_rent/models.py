from django.db import models

# Create your models here.


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

