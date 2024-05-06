from db.models import CinemaHall


def get_cinema_halls():
    return CinemaHall.objects.all()

def create_cinema_hall(hall_name, hall_rows, hall_seats_in_row):
    new_hall = CinemaHall(name=hall_name, rows=hall_rows, seats_in_row=hall_seats_in_row)
    new_hall.save()
    return new_hall
