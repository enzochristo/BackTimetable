from fastapi import APIRouter, Response, Request
from repositories.booking_repository import BookingRepository
from use_cases.customer.my_booking_list.my_booking_list_use_case import MyBookingsUseCase

# Cria um roteador para gerenciar as rotas de reservas
router = APIRouter()

# Instância do repositório de reservas
booking_repository = BookingRepository()

# Instância do caso de uso para buscar reservas
get_bookings_use_case = MyBookingsUseCase(booking_repository)

@router.get("/bookings/booking-list")
def get_bookings(client_id: str, response: Response, request: Request):
    """
    Endpoint para buscar todas as reservas de um cliente específico pelo seu ID.

    Args:
        client_id (str): ID do cliente para o qual as reservas serão buscadas.
        response (Response): Objeto de resposta HTTP.
        request (Request): Objeto de requisição HTTP.

    Returns:
        JSON: Lista de reservas ou mensagem de erro.
    """
    return get_bookings_use_case.execute(client_id, response, request)
