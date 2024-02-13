from django.contrib import admin
from .models import Parcel

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'description', 'weight', 'planned_delivery_date']
    search_fields = ['tracking_number', 'description']
    list_filter = ['planned_delivery_date']
