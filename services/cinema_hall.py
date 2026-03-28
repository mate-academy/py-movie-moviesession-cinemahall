from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    # Return a list of all cinema halls
    # In a real-world scenario, this list might be populated from a database
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:
    # Create a new cinema hall and return it
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row)
    # In a real-world scenario,
    # you might want to store the cinema hall in a
    # database
    return cinema_hall
