from repositories.manager_repository import ManagersRepository
from fastapi import FastAPI, Request, Response
from use_cases.managerr.auth.login.login_dto import LoginDTO
import jwt
import os

class LoginUseCase:
    manager_repository: ManagersRepository

    def __init__(self, manager_repository: ManagersRepository):
        self.manager_repository = manager_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        check_exists = self.manager_repository.find_by_email(email=login_dto.email)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um gerente com o email fornecido"}

        manager = check_exists[0]

        if (not manager.check_password_matches(login_dto.password)):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}

        token = jwt.encode({"email": manager.email, "id": str(manager.id)}, os.getenv("DIRECTOR_JWT_SECRET"))

        response.set_cookie(key="manager_auth_token", value=f"Bearer {token}", httponly=True)
        
        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}
    

