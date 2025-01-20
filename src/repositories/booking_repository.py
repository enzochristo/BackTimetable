from typing import List, Optional
from models.booking_model import BookingsModel  # Modelo de reserva
from entities.booking import Booking


class BookingRepository:
    def save(self, booking: Booking) -> None:
        """
        Salva uma nova reserva no banco de dados.
        """
        booking_model = BookingsModel(**booking.model_dump())
        booking_model.save()

    def find_by_id(self, booking_id: str) -> Optional[BookingsModel]:
        """
        Encontra uma reserva pelo ID.

        Args:
            booking_id (str): ID da reserva.

        Returns:
            Optional[BookingsModel]: A reserva encontrada ou None.
        """
        return BookingsModel.objects(id=booking_id).first()

    def find_all_by_date(self, date: str) -> List[BookingsModel]:
        """
        Retorna todas as reservas para uma data específica.

        Args:
            date (str): Data das reservas.

        Returns:
            List[BookingsModel]: Lista de reservas encontradas.
        """
        return list(BookingsModel.objects(date=date))

    def delete_by_id(self, booking_id: str) -> bool:
        """
        Deleta uma reserva pelo ID.

        Args:
            booking_id (str): ID da reserva.

        Returns:
            bool: True se a reserva foi deletada, False caso não encontrada.
        """
        booking = self.find_by_id(booking_id)
        if booking:
            booking.delete()
            return True
        return False

    def get_booking_by_id(self, booking_id: str) -> Optional[dict]:
        """
        Obtém uma reserva pelo ID e retorna como dicionário.

        Args:
            booking_id (str): ID da reserva.

        Returns:
            Optional[dict]: Dicionário representando a reserva ou None.
        """
        booking = BookingsModel.objects.with_id(booking_id)
        if not booking:
            return None
        booking_dict = booking.to_mongo().to_dict()
        booking_dict['_id'] = str(booking_dict['_id'])
        return booking_dict
