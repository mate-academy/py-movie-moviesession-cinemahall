from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:

    return CinemaHall.objects.create(
        rows=hall_rows,
        name=hall_name,
        seats_in_row=hall_seats_in_row
    )
