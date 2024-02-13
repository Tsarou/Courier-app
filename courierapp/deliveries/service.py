from .dto import DeliveryDTO
from .dao import DeliveryDAO

class DeliveryService:
    @staticmethod
    def create_delivery(delivery_dto):
        delivery = DeliveryDAO.create_delivery(delivery_dto)
        return DeliveryDTO(
            parcel=delivery.parcel,
            customer=delivery.customer,
            delivery_date=delivery.delivery_date,
            status=delivery.status
        )

    @staticmethod
    def get_delivery_by_tracking_number(tracking_number):
        delivery = DeliveryDAO.get_delivery_by_tracking_number(tracking_number)
        if delivery:
            return DeliveryDTO(
                parcel=delivery.parcel,
                customer=delivery.customer,
                delivery_date=delivery.delivery_date,
                status=delivery.status
            )
        else:
            return None

    @staticmethod
    def get_deliveries_by_customer(customer):
        deliveries = DeliveryDAO.get_deliveries_by_customer(customer)
        return [DeliveryDTO(
            parcel=delivery.parcel,
            customer=delivery.customer,
            delivery_date=delivery.delivery_date,
            status=delivery.status
        ) for delivery in deliveries]

    
