from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        rows: int,
        hall_seats_in_row: int
) -> None:
    CinemaHall.objects.create(
        name=hall_name,
        rows=rows,
        seats_in_row=hall_seats_in_row
    )
