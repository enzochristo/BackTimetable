from typing import List, Optional
from mongoengine import *
from entities.customer import Customer
from models.customer_model import CustomersModel
import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class CustomerRepository:
    def save(self, customer: Customer) -> None:
        """Salva um novo cliente no banco de dados."""
        customer_model = CustomersModel()
        customer_dict = customer.model_dump()
        
        for k in CustomersModel.get_normal_fields():
            if (k not in customer_dict):
                continue

            customer_model[k] = customer_dict[k]

        for k in CustomersModel.sensivity_fields:
            customer_model[k] = SensivityField(fernet=self.fernet, data=customer_dict[k])


        customer_model.password = bcrypt.hashpw(f'{customer.password}'.encode(), bcrypt.gensalt()).decode()

        customer_model.save()
        return None

    def find_by_id(self, id: str) -> list[CustomersModel]:
        """Encontra um cliente pelo ID."""
        return CustomersModel.objects(id=id).first()

    def find_by_email(self, email: str) -> list[CustomersModel]:
        """Encontra um cliente pelo email."""
        return CustomersModel.objects(email=email).first()
    

    def get_email(self, id: str) -> str:
        customer = CustomersModel.objects(id=id).first()
        if customer: 
            return customer.email

    def update_name(self, id: str, name: str) -> None:
        """Atualiza o nome do cliente."""
        CustomersModel.objects(id=id).update(set__name=name)
        return None

    def delete(self, id: str) -> None:
        """Deleta um cliente pelo ID."""
        CustomersModel.objects(id=id).delete()
        return None
    
    
