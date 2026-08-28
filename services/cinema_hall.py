from db.models import CinemaHall


def get_cinema_halls():
    cinema_hall = CinemaHall.objects.all()
    return cinema_hall


def create_cinema_hall(
        hall_name: str=None,
        hall_rows: int=None,
        hall_seats_in_row: int=None
) -> CinemaHall:
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
    return cinema_hall