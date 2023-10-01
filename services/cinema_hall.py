from django.db.models.query import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def get_cinemahall_by_id(cinemahall_id: int) -> CinemaHall:
    return CinemaHall.objects.get(id=cinemahall_id)


def create_cinema_hall(
        hall_name: str, hall_rows: int, hall_seats_in_row: int
) -> CinemaHall:
    new_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )

    return new_hall
