from django.urls import path
from .views import ParcelListView, ParcelDetailView, ParcelList, UpdatePlannedDeliveryDateView, ParcelDetailView, UpdateDeliveryDateView

urlpatterns = [
    path('parcels/<str:tracking_number>/', ParcelDetailView.as_view(), name='parcel-detail'),
    path('parcels/<str:tracking_number>/', ParcelDetailView.as_view(), name='parcel_detail'),
    path('parcels/<str:tracking_number>/update-delivery-date/', UpdateDeliveryDateView.as_view(), name='update_delivery_date'),
]
