from db.models import CinemaHall


def get_cinema_halls(cinema_halls: int) -> list[int]:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int) -> CinemaHall:
    return CinemaHall.objects.create(
        hall_name=hall_name,
        hall_row=hall_rows,
        hall_seats_in_row=hall_seats_in_row
    )
