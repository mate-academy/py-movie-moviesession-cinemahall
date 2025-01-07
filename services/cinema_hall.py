from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()

def create_cinema_hall(
        name: str,
        rows: int,
        seat_in_row: int
) -> CinemaHall:
    cinema_hall = CinemaHall().objects.create(
        name = name,
        rows = rows,
        seat_in_row = seat_in_row
    )
    return cinema_hall
