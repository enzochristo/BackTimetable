from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class BookingsModel(Document):
    sensivity_fields = [
        
    ]

    customer_id = StringField(required=True)  # Relaciona ao cliente
    table_id = StringField(required=True)     # Relaciona à mesa
    date = StringField(required=True)         # Data da reserva
    time = StringField(required=True)         # Horário da reserva
    number_of_people = IntField(required=True)



    def get_normal_fields():
        return [i for i in BookingsModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in BookingsModel.sensivity_fields]
    
