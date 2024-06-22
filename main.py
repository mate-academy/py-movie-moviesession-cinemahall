import init_django_orm  # noqa: F401

from db.models import Genre, Actor, Movie, CinemaHall, MovieSession

from services import movie, cinema_hall, movie_session


def main():
    print(cinema_hall.get_cinema_halls()[1].capacity)


if __name__ == "__main__":
    main()
