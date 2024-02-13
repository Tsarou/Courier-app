from django.urls import path
from .views import CustomerListView, CustomerDetailView, CustomerParcelListView, CustomerDashboardView, CustomerParcelsView

urlpatterns = [
    path('customer/dashboard/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('customer/parcels/', CustomerParcelsView.as_view(), name='customer_parcels'),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<str:email>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<str:customer_email>/parcels/', CustomerParcelListView.as_view(), name='customer-parcel-list'),
    
]
