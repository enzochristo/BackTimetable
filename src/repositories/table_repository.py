from typing import List, Optional
from mongoengine import *
from entities.table import Table
from models.table_model import TableModel

class TableRepository:
    def save(self, table: Table) -> None:
        """Salva uma nova mesa no banco de dados."""
        table_model = TableModel(**table.model_dump())
        table_model.save()
        return None

    def find_by_id(self, id: str) -> Optional[TableModel]:
        """Encontra uma mesa pelo ID."""
        return TableModel.objects(id_table=id).first()

    def find_all(self) -> List[TableModel]:
        """Retorna todas as mesas."""
        return list(TableModel.objects)

    def update_status(self, id: str, status: str) -> None:
        """Atualiza o status da mesa (available ou occupied)."""
        TableModel.objects(id_table=id).update(set__status=status)
        return None

    def update_reservation(self, id: str, reservation_id: Optional[str]) -> None:
        """Atualiza a reserva associada à mesa."""
        TableModel.objects(id_table=id).update(set__id_reservation=reservation_id)
        return None

    def delete(self, id: str) -> None:
        """Deleta uma mesa pelo ID."""
        TableModel.objects(id_table=id).delete()
        return None
