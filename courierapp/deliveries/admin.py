from django.contrib import admin
from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['parcel', 'customer', 'delivery_date', 'status']
    search_fields = ['parcel__tracking_number', 'customer__email']
    list_filter = ['delivery_date', 'status']
