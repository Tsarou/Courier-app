from .dto import ParcelDTO
from .dao import ParcelDAO

class ParcelService:
    @staticmethod
    def create_parcel(parcel_dto):
        parcel = ParcelDAO.create_parcel(parcel_dto)
        return ParcelDTO(
            tracking_number=parcel.tracking_number,
            description=parcel.description,
            weight=parcel.weight,
            planned_delivery_date=parcel.planned_delivery_date
        )

    @staticmethod
    def get_parcel(tracking_number):
        parcel = ParcelDAO.get_parcel(tracking_number)
        if parcel:
            return ParcelDTO(
                tracking_number=parcel.tracking_number,
                description=parcel.description,
                weight=parcel.weight,
                planned_delivery_date=parcel.planned_delivery_date
            )
        else:
            return None

    
