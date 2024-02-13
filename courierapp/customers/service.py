from .dto import CustomerDTO
from .dao import CustomerDAO

class CustomerService:
    @staticmethod
    def create_customer(customer_dto):
        customer = CustomerDAO.create_customer(customer_dto)
        return CustomerDTO(
            name=customer.name,
            email=customer.email,
            address=customer.address,
            phone_number=customer.phone_number
        )

    @staticmethod
    def get_customer(email):
        customer = CustomerDAO.get_customer(email)
        if customer:
            return CustomerDTO(
                name=customer.name,
                email=customer.email,
                address=customer.address,
                phone_number=customer.phone_number
            )
        else:
            return None

    
