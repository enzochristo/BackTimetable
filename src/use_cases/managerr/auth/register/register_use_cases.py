from repositories.manager_repository import ManagersRepository
from use_cases.managerr.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.manager import Manager

class RegisterUseCase:
    manager_repository = ManagersRepository

    def __init__(self, manager_repository: ManagersRepository):
        self.manager_repository = manager_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        manager = Manager(**register_dto.model_dump())

        self.manager_repository.save(manager)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do gerente com sucesso"}