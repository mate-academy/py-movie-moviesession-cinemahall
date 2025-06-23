# services/cinema_hall.py

from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    """
    Retorna todas as salas de cinema.

    :return: Um QuerySet de objetos CinemaHall.
    """
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str, hall_rows: int, hall_seats_in_row: int) -> CinemaHall:
    """
    Cria uma nova sala de cinema.

    :param hall_name: O nome da sala de cinema.
    :param hall_rows: O número de fileiras de assentos.
    :param hall_seats_in_row: O número de assentos em cada fileira.
    :return: O objeto CinemaHall recém-criado.
    """
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
    return cinema_hall

