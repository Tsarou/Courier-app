from django.db import models

class Parcel(models.Model):
    tracking_number = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    planned_delivery_date = models.DateField()

    def __str__(self):
        return self.tracking_number
