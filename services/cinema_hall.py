from typing import List
from db.models import CinemaHall


def get_cinema_halls() -> List[CinemaHall]:
    """
    Retrieve all cinema halls from the database.

    Returns:
        List[CinemaHall]: A list of CinemaHall instances.
    """
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:
    """
    Create a new cinema hall and save it to the database.

    Args:
        hall_name (str): The name of the cinema hall.
        hall_rows (int): The number of rows in the cinema hall.
        hall_seats_in_row (int): The number of seats in each row.

    Returns:
        CinemaHall: The created CinemaHall instance.
    """
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
