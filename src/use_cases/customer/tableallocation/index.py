from use_cases.customer.create_booking.create_booking_use_case import CreateBookingUseCase 
from repositories.booking_repository import BookingRepository
from repositories.customer_repository import CustomerRepository
from fastapi import FastAPI, Request, Response
from use_cases.customer.create_booking.create_booking_dto import CreateBookingDTO
from fastapi import APIRouter

router = APIRouter()

booking_repository = BookingRepository()
customer_repository  = CustomerRepository()
customer_createbooking_use_case = CreateBookingUseCase(booking_repository, customer_repository)

@router.post("/customer/create-booking")
def customer_register(register_dto: CreateBookingDTO, response: Response, request: Request):
    return customer_createbooking_use_case.execute(register_dto, response, request)
    