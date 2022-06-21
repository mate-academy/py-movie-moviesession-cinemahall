from db.models import Genre, Actor, Movie, MovieSession, CinemaHall


def create():
    CinemaHall.objects.create(name="Blue", rows=10, seats_in_row=12)
    CinemaHall.objects.create(name="VIP", rows=3, seats_in_row=5)
    Movie.objects.create(title="Matrix", description="Matrix description")
    Movie.objects.create(title="Batman", description="Batman description")


create()
