from repositories.booking_repository import BookingRepository
from repositories.table_repository import TableRepository
from repositories.customer_repository import CustomerRepository  # Para buscar cliente pelo e-mail
from use_cases.customer.create_booking.create_booking_dto import CreateBookingDTO
from fastapi import Request, Response
from entities.booking import Booking


class CreateBookingUseCase:
    def __init__(self, booking_repository: BookingRepository, table_repository: TableRepository, customer_repository: CustomerRepository):
        self.booking_repository = booking_repository
        self.table_repository = table_repository
        self.customer_repository = customer_repository

    def execute(self, create_booking_dto: CreateBookingDTO, response: Response, request: Request):
        # Validação inicial dos dados
        if not create_booking_dto.date or not create_booking_dto.time or not create_booking_dto.number_of_people or not create_booking_dto.email:
            response.status_code = 400
            return {"status": "error", "message": "Faltam informações obrigatórias"}

        # Buscar cliente pelo e-mail
        customer = self.customer_repository.find_by_email(create_booking_dto.email)
        if not customer:
            response.status_code = 404
            return {"status": "error", "message": "Cliente não encontrado"}

        # Buscar mesas disponíveis com capacidade suficiente
        available_tables = [
            table for table in self.table_repository.find_all()
            if table.status == "available" and table.cadeiras >= create_booking_dto.number_of_people
        ]

        # Ordenar mesas pela capacidade (menor primeiro)
        available_tables.sort(key=lambda t: t.cadeiras)

        # Verificar se há mesas disponíveis
        if not available_tables:
            response.status_code = 404
            return {"status": "error", "message": "Nenhuma mesa disponível para o número de pessoas solicitado"}

        # Selecionar a menor mesa disponível
        selected_table = available_tables[0]

        # Atualizar o status da mesa para "occupied"
        self.table_repository.update_status(selected_table._id_table, "occupied")

        # Criar a reserva associada à mesa
        booking = Booking(
            date=create_booking_dto.date,
            time=create_booking_dto.time,
            number_of_people=create_booking_dto.number_of_people,
            customer_id=customer.id,
            table_id=selected_table._id_table  # Associando a mesa alocada
        )
        self.booking_repository.save(booking)

        response.status_code = 201
