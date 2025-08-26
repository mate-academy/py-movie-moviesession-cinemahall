from typing import List
from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    """
    Retrieves all cinema halls from the database.

    Returns:
        QuerySet[CinemaHall]: A queryset containing all CinemaHall objects.
    """
    return CinemaHall.objects.all()


def create_cinema_hall(
    hall_name: str, hall_rows: int, hall_seats_in_row: int
) -> CinemaHall:
    """
    Creates a new cinema hall in the database.

    Args:
        hall_name (str): The name of the cinema hall.
        hall_rows (int): The number of rows in the cinema hall.
        hall_seats_in_row (int): The number of seats in each row.

    Returns:
        CinemaHall: The newly created CinemaHall object.
    """
    return CinemaHall.objects.create(
        name=hall_name, rows=hall_rows, seats_in_row=hall_seats_in_row
    )