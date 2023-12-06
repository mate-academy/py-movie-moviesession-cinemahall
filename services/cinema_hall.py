from db.models import CinemaHall
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet:
    return CinemaHall.object.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:
    CinemaHall.objects.create(
        hall_name=hall_name,
        hall_rows=hall_rows,
        hall_seats_in_row=hall_seats_in_row
    )
