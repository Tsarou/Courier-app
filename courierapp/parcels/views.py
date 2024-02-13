from rest_framework import generics
from .models import Parcel
from .serializers import ParcelSerializer
from .service import ParcelService
from .dto import ParcelDTO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import UpdateDeliveryDateForm
from django.utils import timezone


class ParcelListView(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        parcel_dto = ParcelDTO(
            tracking_number=data['tracking_number'],
            description=data['description'],
            weight=data['weight'],
            planned_delivery_date=data['planned_delivery_date']
        )
        created_parcel = ParcelService.create_parcel(parcel_dto)
        serializer.save(
            tracking_number=created_parcel.tracking_number,
            description=created_parcel.description,
            weight=created_parcel.weight,
            planned_delivery_date=created_parcel.planned_delivery_date
        )

class ParcelDetailView(View):
    def get(self, request, tracking_number):
        parcel = get_object_or_404(Parcel, tracking_number=tracking_number)
        return render(request, 'parcel_detail.html', {'parcel': parcel})

    def get_object(self):
        tracking_number = self.kwargs.get('tracking_number')
        return ParcelService.get_parcel(tracking_number)


class ParcelList(APIView):
    def get(self, request, customer_email):
        try:
            customer_parcels = Parcel.objects.filter(customer__email=customer_email)
            serializer = ParcelSerializer(customer_parcels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class UpdatePlannedDeliveryDateView(APIView):
    def patch(self, request, pk):
        try:
            parcel = Parcel.objects.get(pk=pk)
            new_delivery_date = request.data.get('planned_delivery_date')
            if new_delivery_date <= timezone.now().date():
                return Response({'error': 'Planned delivery date must be in the future'}, status=status.HTTP_400_BAD_REQUEST)
            parcel.planned_delivery_date = new_delivery_date
            parcel.save()
            serializer = ParcelSerializer(parcel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Parcel.DoesNotExist:
            return Response({'error': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class UpdateDeliveryDateView(View):
    def get(self, request, tracking_number):
        parcel = get_object_or_404(Parcel, tracking_number=tracking_number)
        form = UpdateDeliveryDateForm(instance=parcel)
        return render(request, 'update_delivery_date.html', {'form': form, 'parcel': parcel})

    def post(self, request, tracking_number):
        parcel = get_object_or_404(Parcel, tracking_number=tracking_number)
        form = UpdateDeliveryDateForm(request.POST, instance=parcel)
        if form.is_valid():
            form.save()
            return redirect('parcel_detail', tracking_number=tracking_number)
        return render(request, 'update_delivery_date.html', {'form': form, 'parcel': parcel})