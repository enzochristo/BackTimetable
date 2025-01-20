from repositories.booking_repository import BookingRepository
from repositories.table_repository import TableRepository
from use_cases.managerr.tableallocation import CreateBookingManagerDTO
from fastapi import Request, Response
from entities.booking import Booking


class CreateBookingManagerUseCase:
    def __init__(self, booking_repository: BookingRepository, table_repository: TableRepository):
        self.booking_repository = booking_repository
        self.table_repository = table_repository

    def execute(self, create_booking_dto: CreateBookingManagerDTO, response: Response, request: Request):
        # Validação inicial dos dados
        if not create_booking_dto.date or not create_booking_dto.time or not create_booking_dto.number_of_people or not create_booking_dto.table_id:
            response.status_code = 400
            return {"status": "error", "message": "Faltam informações obrigatórias"}

        # Buscar a mesa pelo ID
        table = self.table_repository.find_by_id(create_booking_dto.table_id)
        if not table:
            response.status_code = 404
            return {"status": "error", "message": "Mesa não encontrada"}

        # Verificar disponibilidade da mesa
        if table.status != "available":
            response.status_code = 400
            return {"status": "error", "message": "Mesa já está ocupada"}

        # Verificar capacidade da mesa
        if table.cadeiras < create_booking_dto.number_of_people:
            response.status_code = 400
            return {"status": "error", "message": "Mesa não suporta o número de pessoas"}

        # Atualizar a mesa para "occupied" e associar à reserva
        self.table_repository.update_status(table._id_table, "occupied")

        # Criar a reserva associada à mesa
        booking = Booking(
            date=create_booking_dto.date,
            time=create_booking_dto.time,
            number_of_people=create_booking_dto.number_of_people,
            table_id=table._id_table  # Associando a mesa escolhida
        )
        self.booking_repository.save(booking)

        response.status_code = 201
        return {"status": "success", "message": f"Reserva criada com sucesso para a mesa {table._id_table}"}
