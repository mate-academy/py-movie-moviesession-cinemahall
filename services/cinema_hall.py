import init_django_orm  # noqa: F401
from typing import List
from db.models import CinemaHall


def get_cinema_halls() -> List["CinemaHall"]:
    return list(CinemaHall.objects.all())


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:
    CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats=hall_seats_in_row
    )
