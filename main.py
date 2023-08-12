import datetime
import subprocess

import pytz

# noinspection PyUnresolvedReferences
import init_django_orm
from db.models import Genre, Actor, Movie, CinemaHall, MovieSession


def clear_db():
    _models = [Genre, Actor, Movie, CinemaHall, MovieSession]
    for model in _models:
        model.objects.all().delete()


def load_data(json_file_path):
    command = f"python manage.py loaddata {json_file_path}"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


def main(*args, **kwargs):
    speed = Movie.objects.create(title="Speed", description="Speed movie")
    print(speed)

    blue = CinemaHall.objects.create(name="Blue", rows=9, seats_in_row=13)
    print(blue)  # Blue
    print(blue.capacity)  # 117

    try:
        timezone = pytz.timezone("Europe/Kyiv")
        aware_show_time = timezone.localize(datetime.datetime(
            year=2021,
            month=11,
            day=29,
            hour=16,
            minute=40
        ))
        movie_session = MovieSession.objects.create(
            show_time=aware_show_time,
            cinema_hall=blue,
            movie=speed
        )
        print(movie_session)  # Speed 2021-11-29 16:40:00+01:00
    except RuntimeWarning as warning:
        print(f"Warning: {warning}")


if __name__ == "__main__":
    clear_db()
    load_data("cinema_db_data.json")
    main()
