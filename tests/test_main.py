import pytest
import datetime

from contextlib import redirect_stdout
from io import StringIO

from db.models import Actor, Genre, Movie, MovieSession, CinemaHall
from services.movie import get_movies, get_movie_by_id, create_movie
from services.cinema_hall import get_cinema_halls, create_cinema_hall
from services.movie_session import (
    create_movie_session,
    get_movies_sessions,
    get_movie_session_by_id,
    update_movie_session,
    delete_movie_session_by_id,
)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "title,description,out",
    [
        ("Speed", "Action movie", "Speed\n"),
        ("Harry Potter", "Magic movie", "Harry Potter\n"),
        ("Batman", "Superhero movie", "Batman\n"),
    ],
)
def test_movie_str(title, description, out):
    movie = Movie.objects.create(title=title, description=description)

    f = StringIO()

    with redirect_stdout(f):
        print(movie)

    output = f.getvalue()

    assert out == output


@pytest.mark.django_db
@pytest.mark.parametrize(
    "name,rows,seats_in_row,out",
    [
        ("VIP", 12, 10, "VIP\n"),
        ("Blue", 8, 11, "Blue\n"),
        ("Cheap", 7, 17, "Cheap\n"),
    ],
)
def test_cinema_hall_str(name, rows, seats_in_row, out):
    cinema_hall = CinemaHall.objects.create(
        name=name, rows=rows, seats_in_row=seats_in_row
    )

    f = StringIO()

    with redirect_stdout(f):
        print(cinema_hall)

    output = f.getvalue()

    assert out == output


@pytest.mark.django_db
@pytest.mark.parametrize(
    "name,rows,seats_in_row,capacity",
    [
        ("VIP", 12, 10, 120),
        ("Blue", 8, 11, 88),
        ("Cheap", 7, 17, 119),
    ],
)
def test_cinema_hall_capacity(name, rows, seats_in_row, capacity):
    cinema_hall = CinemaHall.objects.create(
        name=name, rows=rows, seats_in_row=seats_in_row
    )

    assert cinema_hall.capacity == capacity


@pytest.fixture()
@pytest.mark.django_db  # <--- ДОДАНО: ВИПРАВЛЕННЯ OperationalError
def movie_session_database_data():
    movie_sessions = []
    movie = Movie.objects.create(title="Speed", description="None")
    cinema_hall = CinemaHall.objects.create(name="Blue",
                                            rows=10,
                                            seats_in_row=10)
    movie_sessions.append(
        (
            MovieSession.objects.create(
                show_time=datetime.datetime(2022, 2, 22, 15, 30),
                cinema_hall=cinema_hall,
                movie=movie,
            ),
            "Speed 2022-02-22 15:30:00\n",
        )
    )

    movie = Movie.objects.create(title="Harry Potter", description="None")

    movie_sessions.append(
        (
            MovieSession.objects.create(
                show_time=datetime.datetime(2021, 2, 23, 11, 10),
                cinema_hall=cinema_hall,
                movie=movie,
            ),
            "Harry Potter 2021-02-23 11:10:00\n",
        )
    )

    return movie_sessions


@pytest.mark.django_db
def test_movie_session_str(movie_session_database_data):
    for data in movie_session_database_data:
        f = StringIO()

        with redirect_stdout(f):
            print(data[0])

        output = f.getvalue()

        assert output == data[1]


@pytest.fixture()
@pytest.mark.django_db  # <--- ДОДАНО: ВИПРАВЛЕННЯ OperationalError
def database_data():
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Drama")
    western = Genre.objects.create(name="Western")

    reeves = Actor.objects.create(first_name="Keanu", last_name="Reeves")
    johansson = Actor.objects.create(first_name="Scarlett",
                                     last_name="Johansson")
    clooney = Actor.objects.create(first_name="George", last_name="Clooney")

    matrix = Movie.objects.create(title="Matrix", description="Matrix movie")
    matrix.actors.add(reeves)
    matrix.actors.add(johansson)
    matrix.genres.add(action)

    batman = Movie.objects.create(title="Batman", description="Batman movie")
    batman.genres.add(drama)
    batman.actors.add(clooney)

    titanic = Movie.objects.create(title="Titanic",
                                   description="Titanic movie")
    titanic.genres.add(drama, action)

    good_bad = Movie.objects.create(
        title="The Good, the Bad and the Ugly",
        description="The Good, the Bad and the Ugly movie",
    )
    good_bad.genres.add(western)

    blue = CinemaHall.objects.create(name="Blue", rows=10, seats_in_row=12)
    vip = CinemaHall.objects.create(name="VIP", rows=4, seats_in_row=6)
    cheap = CinemaHall.objects.create(name="Cheap", rows=15, seats_in_row=27)

    MovieSession.objects.create(
        show_time=datetime.datetime(2019, 8, 19, 20, 30),
        cinema_hall=blue,
        movie=matrix
    )
    MovieSession.objects.create(
        show_time=datetime.datetime(2017, 8, 19, 11, 10),
        cinema_hall=cheap,
        movie=titanic,
    )
    MovieSession.objects.create(
        show_time=datetime.datetime(2021, 4, 3, 13, 50),
        cinema_hall=vip,
        movie=good_bad
    )

    MovieSession.objects.create(
        show_time=datetime.datetime(2021, 4, 3, 16, 30),
        cinema_hall=cheap,
        movie=matrix
    )


@pytest.mark.django_db
def test_movie_service_get_movies(database_data):
