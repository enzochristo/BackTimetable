from fastapi import Request, Response, Depends
from fastapi import APIRouter
from .check_session import CheckSessionValidatyUseCase
from middlewares.validate_customer_auth_token import validade_customer_auth_token

router = APIRouter()
check_session_validity_use_case = CheckSessionValidatyUseCase()

@router.post("/customer/auth/check/token", dependencies=[Depends(validade_customer_auth_token)])
def check_session_validity(response: Response, request: Request):
    return check_session_validity_use_case.execute(response, request)