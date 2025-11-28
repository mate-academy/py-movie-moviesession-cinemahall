from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
    hall_name: str,
    hall_rows: int,
    hall_seats_in_row: int
) -> CinemaHall:
    if not hall_name or not hall_name.strip():
        raise ValueError("Hall name cannot be empty")

    if hall_rows <= 0:
        raise ValueError("Number of rows must be positive")

    if hall_seats_in_row <= 0:
        raise ValueError("Number of seats per row must be positive")

    cinema_hall = CinemaHall.objects.create(
        name=hall_name.strip(),
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )

    return cinema_hall
