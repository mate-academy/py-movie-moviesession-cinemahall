import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from django.db import DatabaseError
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
    hall_name: str, hall_rows: int, hall_seats_in_row: int
) -> CinemaHall | None:
    try:
        cinema_hall, created = CinemaHall.objects.get_or_create(
            name=hall_name, rows=hall_rows, seats_in_row=hall_seats_in_row
        )
        return cinema_hall
    except DatabaseError:
        return None
