from db.models import CinemaHall


def get_cinema_halls():
    return CinemaHall.objects.all()


def create_cinema_hall(name: str, hall_rows: int, hall_seats_in_row: int):
    CinemaHall.objects.create(name=name, rows=hall_rows,
                              seats_in_row=hall_seats_in_row)
