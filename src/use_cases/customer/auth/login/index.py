from fastapi import Request, Response, Depends
from fastapi import APIRouter
from repositories.customer_repository import CustomerRepository
from use_cases.customer.auth.login.login_dto import LoginDTO
from .login_use_case import LoginUseCase
from middlewares.validate_customer_auth_token import validade_customer_auth_token
from entities.customer import Customer


router = APIRouter()

customer_repository = CustomerRepository()
login_use_case = LoginUseCase(customer_repository)


@router.post("/customer/auth/login", dependencies=[Depends(validade_customer_auth_token)])
def customer_login(customer_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(customer_login_dto, response, request)

