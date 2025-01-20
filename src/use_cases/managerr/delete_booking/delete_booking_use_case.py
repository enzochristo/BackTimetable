from repositories.booking_repository import BookingRepository
from fastapi import Response

class DeleteBookingUseCase:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, booking_id: str, response: Response):
        """
        Remove uma reserva pelo ID.

        Args:
            booking_id (str): ID da reserva.
            response (Response): Resposta HTTP.

        Returns:
            dict: Resultado da operação.
        """
        if not booking_id:
            response.status_code = 400
            return {"status": "error", "message": "Booking ID is required"}

        success = self.booking_repository.delete_by_id(booking_id)
        if not success:
            response.status_code = 404
            return {"status": "error", "message": "Booking not found"}

        response.status_code = 200
        return {"status": "success", "message": "Booking deleted successfully"}
