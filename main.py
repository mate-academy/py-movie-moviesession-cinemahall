import init_django_orm  # noqa: F401

import datetime
from db.models import Genre, Movie, MovieSession, Actor, CinemaHall
from services import movie, cinema_hall, movie_session


def main():
    return movie_session.update_movie_session(session_id=3, movie_id=2, cinema_hall_id=1)


if __name__ == '__main__':
    print(main())
