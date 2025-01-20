from repositories.customer_repository import CustomerRepository
from use_cases.customer.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.customer import Customer

class RegisterUseCase:
    customer_repository = CustomerRepository

    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        customer = Customer(**register_dto.model_dump())

        self.customer_repository.save(customer)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do cliente com sucesso"}