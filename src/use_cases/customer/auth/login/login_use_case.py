from repositories.customer_repository import CustomerRepository
from fastapi import FastAPI, Request, Response
from .login_dto import LoginDTO
from entities.customer import Customer
import jwt
import os

class LoginUseCase:
    costumer_repository = CustomerRepository

    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository
        

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        check_exists = self.customer_repository.find_by_email(email=login_dto.email)
        

        if len(check_exists) == 0:
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um cliente com o email fornecido"}

        customer = check_exists[0]
        

        if not customer.check_password_matches(login_dto.password):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um cliente com o email fornecido"}

        token = jwt.encode({"email": customer.email, "id": str(customer.id)}, os.getenv("APPRAISER_JWT_SECRET"))


        response.set_cookie(key="customer_auth_token", value=f"Bearer {token}", httponly=True)

        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}

