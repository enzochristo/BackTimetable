from repositories.booking_repository import BookingRepository
from fastapi import Request, Response
from typing import Dict, Any

class MyBookingsUseCase:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, customer_id: str, response: Response, request: Request) -> Dict[str, Any]:
        """
        Busca todas as reservas de um cliente específico pelo ID.

        Args:
            customer_id (str): O ID do cliente para o qual as reservas serão buscadas.
            response (Response): Objeto de resposta do FastAPI.
            request (Request): Objeto de requisição do FastAPI.

        Returns:
            Dict[str, Any]: Retorna um dicionário com o status e os dados das reservas.
        """
        try:
            # Busca todas as reservas pelo ID do cliente
            bookings = self.booking_repository.find_all_by_customer_id(customer_id)
            
            # Caso não existam reservas, retorna erro 404
            if not bookings:
                response.status_code = 404
                return {
                    "status": "error",
                    "message": "No bookings found for this customer."
                }

            # Retorna as reservas encontradas com status 200
            response.status_code = 200
            return {
                "status": "success",
                "bookings": bookings  # Retorna a lista de reservas
            }

        except Exception as e:
            # Em caso de erro, retorna um status 500
            response.status_code = 500
            return {
                "status": "error",
                "message": f"An error occurred while fetching bookings: {str(e)}"
            }
