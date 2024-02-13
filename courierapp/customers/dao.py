from .models import Customer

class CustomerDAO:
    @staticmethod
    def create_customer(customer_dto):
        return Customer.objects.create(
            name=customer_dto.name,
            email=customer_dto.email,
            address=customer_dto.address,
            phone_number=customer_dto.phone_number
        )

    @staticmethod
    def get_customer(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None

    
