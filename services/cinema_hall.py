from db.models import CinemaHall


def get_cinema_hall():
    cinema_hall = CinemaHall.objects.all()
    return cinema_hall


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int):
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats=hall_seats_in_row)
    return cinema_hall
