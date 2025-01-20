from fastapi import APIRouter, Response, Request
from repositories.booking_repository import BookingRepository
from repositories.customer_repository import CustomerRepository
from use_cases.customer.create_booking.create_booking_use_case import CreateBookingUseCase
from use_cases.customer.create_booking.create_booking_dto import CreateBookingDTO

router = APIRouter()

# Inicializar os repositórios
booking_repository = BookingRepository()
customer_repository = CustomerRepository()

# Inicializar o caso de uso
customer_createbooking_use_case = CreateBookingUseCase(BookingRepository(),CustomerRepository())

@router.post("/customer/create-booking")
def customer_create_booking(create_booking_dto: CreateBookingDTO, response: Response, request: Request):
    return customer_createbooking_use_case.execute(create_booking_dto, response, request)
