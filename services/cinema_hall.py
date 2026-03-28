import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import CinemaHall


def create_cinema_hall(
        hall_name: str, hall_rows: int,
        hall_seats_in_row: int) -> QuerySet:
    """
    Create new cinema hall
    """
    return CinemaHall.objects.create(
        name=hall_name, rows=hall_rows, seats_in_row=hall_seats_in_row
    )


def get_cinema_halls() -> QuerySet:
    """
    Retrieve list of all cinema halls
    """
    return CinemaHall.objects.all()
