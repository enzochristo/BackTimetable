from mongoengine import *
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class CustomerModel(Document):
    sensivity_fields = [
        "password"
    ]

    # Campos do cliente
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True, unique = True)
    phone = StringField(default="")
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)

    meta = {
        "collection": "customers",
        "indexes": [
            {"fields": ["email"], "unique": True},  # Index para e-mails únicos
        ]
    }

    @staticmethod
    def get_normal_fields():
        """
        Retorna os campos que não são considerados sensíveis.
        """
        return [
            i for i in CustomerModel.__dict__.keys()
            if i[:1] != '_' and i != "sensivity_fields" and i not in CustomerModel.sensivity_fields
        ]

    def get_decrypted_field(self, field: str):
        """
        Retorna o valor de um campo sensível descriptografado.
        """
        if field not in self.sensivity_fields:
            raise Exception("Campo não está mapeado como sensível")
        encrypted_value = getattr(self, field, None)
        if not encrypted_value:
            return None
        return fernet.decrypt(encrypted_value.encode()).decode()

    def encrypt_password(self):
        """
        Criptografa a senha do cliente antes de salvar.
        """
        self.password = bcrypt.hashpw(self.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password_matches(self, password: str):
        """
        Verifica se a senha fornecida corresponde à senha armazenada.
        """
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def clean(self):
        """
        Método chamado antes de salvar o documento. Aqui criptografamos a senha.
        """
        if self.password and not self.password.startswith("$2b$"):
            self.encrypt_password()
