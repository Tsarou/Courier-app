from rest_framework import generics
from .models import Delivery
from .serializers import DeliverySerializer
from .service import DeliveryService
from .dto import DeliveryDTO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TrackParcelForm, UpdateDeliveryDateForm
from .models import Parcel
from django.shortcuts import render, get_object_or_404
from .models import Parcel, Delivery
from .forms import TrackParcelForm, UpdateDeliveryDateForm
from django.utils import timezone

def update_delivery_date(request, tracking_number):
    parcel = get_object_or_404(Parcel, tracking_number=tracking_number)

    if request.method == 'POST':
        form = UpdateDeliveryDateForm(request.POST)
        if form.is_valid():
            new_delivery_date = form.cleaned_data['new_delivery_date']
            # Check if the selected delivery date is in the future
            if new_delivery_date <= timezone.now().date():
                form.add_error('new_delivery_date', 'Please select a future date.')
            else:
                # Update the delivery date in the database
                parcel.planned_delivery_date = new_delivery_date
                parcel.save()
                # Redirect to the homepage or a success page
                return render(request, 'delivery_updated.html', {'tracking_number': tracking_number})
    else:
        form = UpdateDeliveryDateForm()

    return render(request, 'update_delivery_date.html', {'form': form, 'parcel': parcel, 'tracking_number': tracking_number})



def homepage(request):
    form = TrackParcelForm()

    if request.method == 'POST':
        form = TrackParcelForm(request.POST)
        if form.is_valid():
            tracking_number = form.cleaned_data['tracking_number']
            try:
                parcel = Parcel.objects.get(tracking_number=tracking_number)
                delivery = Delivery.objects.get(parcel=parcel)
                return render(request, 'homepage.html', {'form': form, 'parcel': parcel,'delivery': delivery})
            except Parcel.DoesNotExist:
                form.add_error('tracking_number', 'Parcel not found. Please check the tracking number.')

    return render(request, 'homepage.html', {'form': form})


