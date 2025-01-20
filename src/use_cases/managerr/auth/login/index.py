from use_cases.managerr.auth.login.login_use_case import LoginUseCase
from repositories.manager_repository import ManagersRepository
from fastapi import FastAPI, Request, Response
from use_cases.managerr.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

manager_repository = ManagersRepository()
login_use_case = LoginUseCase(manager_repository)

@router.post("/managerr/auth/login")
def manager_repository(manager_repository: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(manager_repository, response, request)
    