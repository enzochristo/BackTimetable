from mongoengine import Document, StringField, IntField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class ManagersModel(Document):
    # Define sensitive fields for encryption/decryption
    sensivity_fields = [
       
    ]

    # Fields
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)  # Hashed password
    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)

    @staticmethod
    def get_normal_fields():
        """
        Returns all normal (non-sensitive) fields of the model.
        """
        return [
            field for field in ManagersModel.__dict__.keys()
            if field[:1] != '_' and field != "sensivity_fields" and field not in ManagersModel.sensivity_fields
        ]

    def get_decrypted_field(self, field: str):
        """
        Decrypts and returns the value of a sensitive field.
        """
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped for decryption")

        encrypted_value = getattr(self, field, None)
        if encrypted_value:
            return fernet.decrypt(encrypted_value.encode()).decode()
        return None

    def encrypt_field(self, field: str):
        """
        Encrypts the value of a sensitive field and updates the model.
        """
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped for encryption")

        value = getattr(self, field, None)
        if value:
            encrypted_value = fernet.encrypt(value.encode()).decode()
            setattr(self, field, encrypted_value)

    def check_password_matches(self, password: str) -> bool:
        """
        Checks if a given plain-text password matches the hashed password stored.
        """
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def hash_password(self):
        """
        Hashes the plain-text password and updates the model.
        """
        if self.password:
            self.password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt()).decode()
