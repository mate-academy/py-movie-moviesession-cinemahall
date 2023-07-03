from db.models import CinemaHall


def get_cinema_halls():
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str, hall_raws: int, hall_seats_in_row: int) -> None:
    CinemaHall.objects.create(name=hall_name, rows=hall_raws, seats_in_row=hall_seats_in_row)
