from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    """
    Returns all cinema halls.

    :return: QuerySet of all cinema halls
    """
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:
    """
    Creates a new cinema hall.

    :param hall_name: Cinema hall name
    :param hall_rows: Number of rows
    :param hall_seats_in_row: Number of seats per row
    :return: Created CinemaHall object
    """
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
