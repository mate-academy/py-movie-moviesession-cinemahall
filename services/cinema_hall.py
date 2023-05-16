from db.models import CinemaHall
from typing import Optional


def get_cinema_halls() -> Optional[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> Optional[CinemaHall]:
    cinema_hall = CinemaHall(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
    cinema_hall.save()
    return cinema_hall
