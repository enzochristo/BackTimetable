import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.manager import Manager
from models.manager_model import ManagersModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class ManagersRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, manager: Manager) -> None:
        manager_model = ManagersModel()
        manager_dict = manager.model_dump()

        for k in ManagersModel.get_normal_fields():
            if (k not in manager_dict):
                continue

            manager_model[k] = manager_dict[k]

        for k in ManagersModel.sensivity_fields:
            manager_model[k] = SensivityField(fernet=self.fernet, data=manager_dict[k])

        manager_model.password = bcrypt.hashpw(f'{manager.password}'.encode(), bcrypt.gensalt()).decode()

        manager_model.save()

        return None
    
    def find_by_email(self, email: str) -> list[ManagersModel]:
        result = ManagersModel.objects(email=email)
        return result
    
    def find_by_id(self, id: str) -> list[ManagersModel]:
        result = ManagersModel.objects(id=id)
        return result
    
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        ManagersModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[ManagersModel]:
        result: list[ManagersModel] = ManagersModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        ManagersModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        manager = ManagersModel.objects(id=id).first()
        if manager:
            return manager.name

    def get_email(self, id: str) -> str:
        manager = ManagersModel.objects(id=id).first()
        if manager:
            return manager.email
    
    def update_name(self, id: str, name: str) -> None:
        ManagersModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        ManagersModel.objects(id=id).update(set__email = email)
        return None