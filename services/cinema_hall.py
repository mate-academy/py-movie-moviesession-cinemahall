from django.db.models import QuerySet

from db.models import CinemaHall

def get_cinema_halls() -> QuerySet:
    queryset = CinemaHall.objects.all()
    return queryset

def create_cinema_hall(hall_name: str,
           hall_rows: int,
           hall_seats_in_row) -> CinemaHall:
    new_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
       )
    return new_hall