from django.contrib import admin
from django.urls import path, include
from customers.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parcels/', include('parcels.urls')),
    path('customers/', include('customers.urls')),
    path('deliveries/', include('deliveries.urls')),
    #path('', homepage, name='homepage'),
    path('', include('deliveries.urls')),
]
