from typing import List

from db.models import CinemaHall


# Retrieve Cinema Halls
def get_cinema_halls() -> List[object]:
    return CinemaHall.objects.all()


# Create Cinema Hall
def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:
    return CinemaHall.objects.create(
        hall_name=hall_name,
        hall_rows=hall_rows,
        hall_seats_in_row=hall_seats_in_row
    )
