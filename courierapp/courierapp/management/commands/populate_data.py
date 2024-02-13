import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from parcels.models import Parcel
from customers.models import Customer
from deliveries.models import Delivery
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Populate the database with parcels, customers, and deliveries'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating database...'))

        # Populate customers
        customers = []
        for _ in range(20):
            customer = Customer.objects.create(
                name=f'Customer{_ + 1}',
                email=f'customer{_ + 1}@example.com',
                address=f'Address {_ + 1}',
                phone_number=f'123-456-{1000 + _}'
            )
            customers.append(customer)

        # Populate parcels and deliveries
        for _ in range(40):
            customer = random.choice(customers)

            # Generate a random planned delivery date within the next 10 days
            planned_delivery_date = datetime.now() + timedelta(days=random.randint(1, 10))

            # Create a parcel
            parcel = Parcel.objects.create(
                tracking_number=get_random_string(length=8).upper(),
                description=f'Description for parcel {_ + 1}',
                weight=random.uniform(1, 10),
                planned_delivery_date=planned_delivery_date
            )

            # Create a delivery
            delivery = Delivery.objects.create(
                parcel=parcel,
                customer=customer,
                delivery_date=planned_delivery_date,
                status='Pending'  # Default status
            )

            self.stdout.write(self.style.SUCCESS(f'Created Parcel {parcel.tracking_number} for Customer {customer.name}'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
