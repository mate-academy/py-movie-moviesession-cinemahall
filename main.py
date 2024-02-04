import init_django_orm  # noqa: F401

import datetime
from db.models import Genre, Movie, MovieSession, Actor, CinemaHall
from services import movie, cinema_hall, movie_session


def main():
    return movie_session.get_movie_session_by_id(movie_id=3)


if __name__ == '__main__':
    print(main())
