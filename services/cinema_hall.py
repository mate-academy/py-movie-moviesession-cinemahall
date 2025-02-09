# cinema_hall.py

from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    """_summary_
    get_cinema_halls, returns all cinema halls

    Returns:
        QuerySet: _description_
    """
    return CinemaHall.objects.all()


def create_cinema_hall(
    hall_name: str,
    hall_rows: int,
    hall_seats_in_row: int
) -> CinemaHall:
    """_summary_
    create_cinema_hall, takes hall_name, hall_rows, hall_seats_in_row, creates
    cinema hall with provided parameters

    Args:
        hall_name (str): _description_
        hall_rows (int): _description_
        hall_seats_in_row (int): _description_

    Returns:
        CinemaHall: _description_
    """
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
