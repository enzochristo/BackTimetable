from use_cases.customer.auth.register.register_use_case import RegisterUseCase
from repositories.customer_repository import CustomerRepository
from fastapi import FastAPI, Request, Response
from use_cases.customer.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter

router = APIRouter()

customer_repository = CustomerRepository()
customer_register_use_case = RegisterUseCase(customer_repository)

@router.post("/customer/auth/register")
def customer_register(register_dto: RegisterDTO, response: Response, request: Request):
    return customer_register_use_case.execute(register_dto, response, request)
    