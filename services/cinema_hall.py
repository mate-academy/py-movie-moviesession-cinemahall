import init_django_orm  # noqa: F401

from db.models import CinemaHall


def create_cinema_hall(
        hall_name: str, hall_rows: int,
        hall_seats_in_row: int) -> object:
    """
    Create new cinema hall
    """
    new_create_cinema_hall = CinemaHall.objects.create(
        name=hall_name, rows=hall_rows, seats_in_row=hall_seats_in_row
    )

    return new_create_cinema_hall


def get_cinema_halls() -> object:
    """
    Retrieve list of all cinema halls
    """
    queryset = CinemaHall.objects.all()

    return queryset
