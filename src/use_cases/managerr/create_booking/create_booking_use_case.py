from repositories.booking_repository import BookingRepository
from repositories.customer_repository import CustomerRepository  # Repositório para buscar cliente
from use_cases.customer.create_booking.create_booking_dto import CreateBookingDTO
from fastapi import Request, Response
from entities.booking import Booking

class CreateBookingUseCase:
    def __init__(self, booking_repository: BookingRepository, customer_repository: CustomerRepository):
        self.booking_repository = booking_repository
        self.customer_repository = customer_repository

    def execute(self, create_booking_dto: CreateBookingDTO, response: Response, request: Request):
        # Validação dos dados
        if not create_booking_dto.date or not create_booking_dto.number_of_people or not create_booking_dto.time or not create_booking_dto.email:
            response.status_code = 407
            return {"status": "error", "message": "Faltam informações"}

        # Buscar cliente pelo e-mail
        customer = self.customer_repository.find_by_email(create_booking_dto.email)
        if not customer:
            response.status_code = 404
            return {"status": "error", "message": "Cliente não encontrado"}

        # Criar a reserva vinculada ao cliente
        booking = Booking(
            date=create_booking_dto.date,
            time=create_booking_dto.time,
            number_of_people=create_booking_dto.number_of_people,
            customer_id=customer.id  # Conexão com o cliente
        )

        self.booking_repository.save(booking)
        response.status_code = 201
        return {"status": "success", "message": f"Reserva criada para o cliente {create_booking_dto.email}"}
