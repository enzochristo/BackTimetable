from use_cases.managerr.auth.register.register_use_cases import RegisterUseCase
from repositories.manager_repository import ManagersRepository
from fastapi import FastAPI, Request, Response
from use_cases.managerr.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter

router = APIRouter()

manager_repository = ManagersRepository()
register_use_case = RegisterUseCase(manager_repository)

@router.post("/managerr/auth/register")
def manager_repository(manager_repository: RegisterDTO, response: Response, request: Request):
    return register_use_case.execute(manager_repository, response, request)
    