from fastapi import APIRouter, Response
from use_cases.managerr.delete_booking.delete_booking_use_case import DeleteBookingUseCase
from repositories.booking_repository import BookingRepository

router = APIRouter()

# Instância do repositório
booking_repository = BookingRepository()

# Instância do caso de uso
delete_booking_use_case = DeleteBookingUseCase(booking_repository)

@router.delete("/managerr/booking/delete")
def delete_booking(booking_id: str, response: Response):
    """
    Endpoint para deletar uma reserva pelo ID.

    Args:
        booking_id (str): ID da reserva a ser deletada.
        response (Response): Objeto de resposta HTTP.

    Returns:
        dict: Resultado da operação.
    """
    return delete_booking_use_case.execute(booking_id, response)
