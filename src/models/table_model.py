from mongoengine import Document, StringField, IntField, ReferenceField, OptionalField

class Table(Document):
    meta = {"collection": "tables"}  # Define a coleção no MongoDB
    id_table = StringField(required=True, unique=True)  # Identificador único da mesa
    id_reservation = StringField(required=False)  # Relacionamento com a reserva (se ocupado)
    cadeiras = IntField(required=True, min_value=1)  # Número de cadeiras
    status = StringField(required=True, choices=["available", "ocupied"])  # Status da mesa
