from db.models import CinemaHall


def get_cinema_halls():
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name, hall_rows, hall_seats_in_row):
    """
    Creates a new cinema hall with the provided name, number of rows,
    and number of seats per row.
    """
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        capacity=hall_rows * hall_seats_in_row  # Calculate capacity
    )
    return cinema_hall
