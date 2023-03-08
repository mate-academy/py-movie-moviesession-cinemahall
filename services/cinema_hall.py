from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int,
) -> None:
    if not CinemaHall.objects.filter(name=hall_name).exists():
        new_cinema_hall = CinemaHall.objects.create(
            name=hall_name,
            rows=hall_rows,
            seats_in_row=hall_seats_in_row
        )
        print(f"{new_cinema_hall.name} was created!")
    else:
        print(f"Cinema Hall with name: {hall_name} is already exists!!!")
