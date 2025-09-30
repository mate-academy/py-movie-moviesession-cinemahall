from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:
    cinema_hall, create = CinemaHall.objects.get_or_create(
        name=hall_name,
        defaults={
            "rows": hall_rows,
            "seats_in_row": hall_seats_in_row
        }
    )
    if not create:
        print(f"The cinema hall with name: '{hall_name}' already exist!")
    return cinema_hall
