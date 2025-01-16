from mongoengine import EmbeddedDocument, StringField
from cryptography.fernet import Fernet
from utils.encode_hmac_hash import encode_hmac_hash
import dotenv

dotenv.load_dotenv()

class SensitivityField(EmbeddedDocument):
    """
    Campo que permite armazenar dados sensíveis de forma criptografada.
    """
    token = StringField(required=False)  # Dados criptografados
    comparison_hash = StringField(required=False)  # Hash para comparação de valores

    def __init__(self, fernet: Fernet = None, data=None, *args, **kwargs):
        """
        Inicializa o campo sensível com criptografia.
        
        :param fernet: Instância de Fernet para criptografia.
        :param data: Dados a serem armazenados no campo.
        """
        super(SensitivityField, self).__init__(*args, **kwargs)

        if not fernet or data is None:
            return

        # Processa o dado se for uma lista
        if isinstance(data, list):
            self.token = [fernet.encrypt(item.encode()).decode() for item in data]
            self.comparison_hash = [encode_hmac_hash(item) for item in data]
        else:
            # Processa o dado se for um único valor
            self.token = fernet.encrypt(data.encode()).decode()
            self.comparison_hash = encode_hmac_hash(data)

    def verify(self, data: str) -> bool:
        """
        Verifica se o dado fornecido corresponde ao hash armazenado.

        :param data: Dado a ser verificado.
        :return: True se os dados forem equivalentes, False caso contrário.
        """
        return encode_hmac_hash(data) == self.comparison_hash
