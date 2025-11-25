from db.models import CinemaHall


def get_cinema_halls():
    cinema_halls = CinemaHall.objects.all()
    return cinema_halls

def create_cinema_hall(hall_name, hall_rows, hall_seats_in_row):
    cinema_hall = CinemaHall.objects.create(
        title=hall_name,
        hall_rows=hall_rows,
        hall_seats_in_row=hall_seats_in_row
    )
    cinema_hall.save()
