from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from .service import CustomerService
from .dto import CustomerDTO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parcels.models import Parcel 
from django.shortcuts import render
from django.views import View
from parcels.serializers import ParcelSerializer

class CustomerDashboardView(View):
    def get(self, request):
        return render(request, 'customer_dashboard.html', context={})

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        customer_dto = CustomerDTO(
            name=data['name'],
            email=data['email'],
            address=data['address'],
            phone_number=data['phone_number']
        )
        created_customer = CustomerService.create_customer(customer_dto)
        serializer.save(
            name=created_customer.name,
            email=created_customer.email,
            address=created_customer.address,
            phone_number=created_customer.phone_number
        )

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_object(self):
        email = self.kwargs.get('email')
        return CustomerService.get_customer(email)


class CustomerParcelListView(APIView):
    def get(self, request, customer_email):
        try:
            customer_parcels = Parcel.objects.filter(customer__email=customer_email)
            serializer = ParcelSerializer(customer_parcels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CustomerParcelsView(View):
    def get(self, request):
        customer_parcels = Parcel.objects.filter(customer=request.user.customer)
        return render(request, 'customer_parcels.html', {'parcels': customer_parcels})
    


def homepage(request):
    return render(request, 'homepage.html')