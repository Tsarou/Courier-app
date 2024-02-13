from .models import Parcel

class ParcelDAO:
    @staticmethod
    def create_parcel(parcel_dto):
        return Parcel.objects.create(
            tracking_number=parcel_dto.tracking_number,
            description=parcel_dto.description,
            weight=parcel_dto.weight,
            planned_delivery_date=parcel_dto.planned_delivery_date
        )

    @staticmethod
    def get_parcel(tracking_number):
        try:
            return Parcel.objects.get(tracking_number=tracking_number)
        except Parcel.DoesNotExist:
            return None

    
