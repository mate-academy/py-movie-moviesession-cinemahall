from typing import Optional

from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: Optional[str] = None,
        hall_rows: Optional[int] = None,
        hall_seats_in_row: Optional[int] = None,
) -> CinemaHall:
    new_cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row,
    )
    return new_cinema_hall
