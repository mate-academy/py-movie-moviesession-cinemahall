# cinema_hall.py

from db.models import CinemaHall
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet:
    """
    Retrieve all cinema halls.

    :return: QuerySet of all cinema halls
    """
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str, hall_rows: int, hall_seats_in_row: int) -> CinemaHall:
    """
    Create a cinema hall with the provided parameters.

    :param hall_name: Name of the cinema hall
    :param hall_rows: Number of rows in the cinema hall
    :param hall_seats_in_row: Number of seats per row in the cinema hall
    :return: Created CinemaHall object
    """
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )

    return cinema_hall
