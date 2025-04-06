import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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


# Тестирование строкового представления фильма
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


# Тестирование строкового представления кинотеатра
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


# Проверка правильности вычисления вместимости кинотеатра
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


# Фикстура для данных сеансов фильмов
@pytest.fixture()
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


# Тестирование строкового представления сеанса фильма
@pytest.mark.django_db
def test_movie_session_str(movie_session_database_data):
    for data in movie_session_database_data:
        f = StringIO()

        with redirect_stdout(f):
            print(data[0])

        output = f.getvalue()

        assert output == data[1]


# Проверка получения фильмов с жанрами и актерами
@pytest.mark.django_db
def test_movie_service_get_movies_with_genres_and_actors(database_data):
    assert list(
        get_movies(genres_ids=[1, 2], actors_ids=[2, 3]).values_list("title")
    ) == [("Matrix",), ("Batman",)]
    assert list(
        get_movies(genres_ids=[1, 3], actors_ids=[1, 3]).values_list("title")
    ) == [("Matrix",)]


# Проверка создания фильма
@pytest.mark.django_db
def test_movie_service_create_movie():
    create_movie(movie_title="Matrix", movie_description="Matrix description")
    create_movie(movie_title="Batman", movie_description="Batman description")
    assert list(Movie.objects.all().values_list("title", "description")) == [
        ("Matrix", "Matrix description"),
        ("Batman", "Batman description"),
    ]


# Проверка создания фильма с жанрами
@pytest.mark.django_db
def test_movie_service_create_movie_with_genres():
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")
    create_movie(
        movie_title="Matrix",
        movie_description="Matrix description",
        genres_ids=[1]
    )
    create_movie(
        movie_title="Batman",
        movie_description="Batman description",
        genres_ids=[2]
    )

    assert list(
        Movie.objects.filter(
            genres__id__in=[1, 2]).values_list("title", "description")
    ) == [("Matrix", "Matrix description"), ("Batman", "Batman description")]


# Проверка получения сеансов фильмов
@pytest.mark.django_db
def test_movie_session_service_get_movies_sessions(database_data):
    assert list(
        get_movies_sessions().values_list(
            "show_time__date", "cinema_hall__name", "movie__title"
        )
    ) == [
        (datetime.date(2019, 8, 19), "Blue", "Matrix"),
        (datetime.date(2017, 8, 19), "Cheap", "Titanic"),
        (datetime.date(2021, 4, 3), "VIP", "The Good, the Bad and the Ugly"),
        (datetime.date(2021, 4, 3), "Cheap", "Matrix"),
    ]


# Тестирование удаления сеансов фильмов
@pytest.mark.django_db
def test_movie_session_service_delete_movie_session_by_id(database_data):
    delete_movie_session_by_id(1)
    delete_movie_session_by_id(4)

    assert list(
        get_movies_sessions().values_list(
            "show_time__date", "cinema_hall__name", "movie__title"
        )
    ) == [
        (datetime.date(2017, 8, 19), "Cheap", "Titanic"),
        (datetime.date(2021, 4, 3), "VIP", "The Good, the Bad and the Ugly"),
    ]