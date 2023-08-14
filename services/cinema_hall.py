from django.db import IntegrityError
from django.db.models.query import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:
    try:
        CinemaHall.objects.get_or_create(
            name=hall_name,
            rows=hall_rows,
            seats_in_row=hall_seats_in_row
        )
    except IntegrityError as e:
        print(f"{CinemaHall.objects.get(name=hall_name)} cinema hall "
              f"already exists: {e}")
