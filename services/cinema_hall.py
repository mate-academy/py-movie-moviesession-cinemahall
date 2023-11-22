from db.models import CinemaHall

from typing import Any


def get_cinema_halls() -> Any:
    return CinemaHall.objects.all()


def create_cinema_hall(
    hall_name: str,
    hall_rows: int,
    hall_seats_in_row: int
) -> Any:
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
