from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str = None,
        hall_rows: int = None,
        hall_seats_in_row: int = None,
) -> None:

    CinemaHall.objects.get_or_create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row,
    )
