from .models import Delivery

class DeliveryDAO:
    @staticmethod
    def create_delivery(delivery_dto):
        return Delivery.objects.create(
            parcel=delivery_dto.parcel,
            customer=delivery_dto.customer,
            delivery_date=delivery_dto.delivery_date,
            status=delivery_dto.status
        )

    @staticmethod
    def get_delivery_by_tracking_number(tracking_number):
        try:
            return Delivery.objects.get(parcel__tracking_number=tracking_number)
        except Delivery.DoesNotExist:
            return None

    @staticmethod
    def get_deliveries_by_customer(customer):
        return Delivery.objects.filter(customer=customer)
