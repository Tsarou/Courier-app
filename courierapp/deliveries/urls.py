from django.urls import path
from .views import homepage, update_delivery_date

urlpatterns = [
    path('', homepage, name='homepage'),
    path('update-delivery-date/<tracking_number>/', update_delivery_date, name='update_delivery_date'),
]
