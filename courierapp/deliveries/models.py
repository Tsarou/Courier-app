from django.db import models
from parcels.models import Parcel
from customers.models import Customer

class Delivery(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('InTransit', 'In Transit'),
        ('Delivered', 'Delivered'),
    ]

    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    

    def __str__(self):
        return f"{self.parcel.tracking_number} - {self.customer.name}"
