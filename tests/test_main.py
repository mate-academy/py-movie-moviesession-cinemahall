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
def movie_session_database_data():
    movie_sessions = []
    movie = Movie.objects.create(title="Speed", description="None")
    cinema_hall = CinemaHall.objects.create(name="Blue", rows=10, seats_in_row=10)
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
def database_data():
    action = Genre.objects.create(name="Action")
    drama = Genre.objects.create(name="Drama")
    western = Genre.objects.create(name="Western")

    reeves = Actor.objects.create(first_name="Keanu", last_name="Reeves")
    johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")
    clooney = Actor.objects.create(first_name="George", last_name="Clooney")

    matrix = Movie.objects.create(title="Matrix", description="Matrix movie")
    matrix.actors.add(reeves)
    matrix.actors.add(johansson)
    matrix.genres.add(action)

    batman = Movie.objects.create(title="Batman", description="Batman movie")
    batman.genres.add(drama)
    batman.actors.add(clooney)

    titanic = Movie.objects.create(title="Titanic", description="Titanic movie")
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
        show_time=datetime.datetime(2019, 8, 19, 20, 30), cinema_hall=blue, movie=matrix
    )
    MovieSession.objects.create(
        show_time=datetime.datetime(2017, 8, 19, 11, 10),
        cinema_hall=cheap,
        movie=titanic,
    )
    MovieSession.objects.create(
        show_time=datetime.datetime(2021, 4, 3, 13, 50), cinema_hall=vip, movie=good_bad
    )

    MovieSession.objects.create(
        show_time=datetime.datetime(2021, 4, 3, 16, 30), cinema_hall=cheap, movie=matrix
    )


@pytest.mark.django_db
def test_movie_service_get_movies(database_data):
    assert list(get_movies().values_list("title", "description")) == [
        ("Matrix", "Matrix movie"),
        ("Batman", "Batman movie"),
        ("Titanic", "Titanic movie"),
        ("The Good, the Bad and the Ugly", "The Good, the Bad and the Ugly movie"),
    ]


@pytest.mark.django_db
def test_movie_service_get_movies_with_genres_and_actors(database_data):
    assert list(
        get_movies(genres_ids=[1, 2], actors_ids=[2, 3]).values_list("title")
    ) == [("Matrix",), ("Batman",)]
    assert list(
        get_movies(genres_ids=[1, 3], actors_ids=[1, 3]).values_list("title")
    ) == [("Matrix",)]


@pytest.mark.django_db
def test_movie_service_get_movies_with_genres(database_data):
    assert list(get_movies(genres_ids=[1]).values_list("title")) == [
        ("Matrix",),
        ("Titanic",),
    ]
    assert list(get_movies(genres_ids=[2, 3]).values_list("title")) == [
        ("Batman",),
        ("Titanic",),
        ("The Good, the Bad and the Ugly",),
    ]


@pytest.mark.django_db
def test_movie_service_get_movies_with_actors(database_data):
    assert list(get_movies(actors_ids=[1]).values_list("title")) == [("Matrix",)]
    assert list(get_movies(actors_ids=[2, 3]).values_list("title")) == [
        ("Matrix",),
        ("Batman",),
    ]


@pytest.mark.django_db
def test_movie_service_get_movie_by_id(database_data):
    assert get_movie_by_id(1).title == "Matrix"
    assert get_movie_by_id(1).description == "Matrix movie"
    assert get_movie_by_id(3).title == "Titanic"
    assert get_movie_by_id(3).description == "Titanic movie"


@pytest.mark.django_db
def test_movie_service_create_movie():
    create_movie(movie_title="Matrix", movie_description="Matrix description")
    create_movie(movie_title="Batman", movie_description="Batman description")
    assert list(Movie.objects.all().values_list("title", "description")) == [
        ("Matrix", "Matrix description"),
        ("Batman", "Batman description"),
    ]


@pytest.mark.django_db
def test_movie_service_create_movie_with_genres():
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")
    create_movie(
        movie_title="Matrix", movie_description="Matrix description", genres_ids=[1]
    )
    create_movie(
        movie_title="Batman", movie_description="Batman description", genres_ids=[2]
    )

    assert list(
        Movie.objects.filter(genres__id__in=[1, 2]).values_list("title", "description")
    ) == [("Matrix", "Matrix description"), ("Batman", "Batman description")]

    assert list(
        Movie.objects.filter(genres__id__in=[2]).values_list("title", "description")
    ) == [("Batman", "Batman description")]


@pytest.mark.django_db
def test_movie_service_create_movie_with_actors():
    Actor.objects.create(first_name="Keanu", last_name="Reeves")
    Actor.objects.create(first_name="George", last_name="Clooney")
    create_movie(
        movie_title="Matrix", movie_description="Matrix description", actors_ids=[2]
    )
    create_movie(
        movie_title="Batman", movie_description="Batman description", actors_ids=[1]
    )

    assert list(
        Movie.objects.filter(actors__id__in=[1, 2]).values_list("title", "description")
    ) == [("Batman", "Batman description"), ("Matrix", "Matrix description")]

    assert list(
        Movie.objects.filter(actors__id__in=[2]).values_list("title", "description")
    ) == [("Matrix", "Matrix description")]


@pytest.mark.django_db
def test_movie_service_create_movie_with_genres_and_actors():
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")
    Actor.objects.create(first_name="Keanu", last_name="Reeves")
    Actor.objects.create(first_name="George", last_name="Clooney")
    create_movie(
        movie_title="Matrix",
        movie_description="Matrix description",
        genres_ids=[1],
        actors_ids=[2],
    )
    create_movie(
        movie_title="Batman",
        movie_description="Batman description",
        genres_ids=[2],
        actors_ids=[1],
    )

    assert list(
        Movie.objects.filter(genres__id__in=[1, 2], actors__id__in=[1, 2]).values_list(
            "title", "description"
        )
    ) == [("Batman", "Batman description"), ("Matrix", "Matrix description")]

    assert (
        list(
            Movie.objects.filter(genres__id__in=[1], actors__id__in=[1]).values_list(
                "title", "description"
            )
        )
        == []
    )


@pytest.mark.django_db
def test_cinema_hall_service_get_cinema_halls(database_data):
    assert list(get_cinema_halls().values_list("name", "rows", "seats_in_row")) == [
        ("Blue", 10, 12),
        ("VIP", 4, 6),
        ("Cheap", 15, 27),
    ]


@pytest.mark.django_db
def test_cinema_hall_service_create_cinema_hall():
    create_cinema_hall(hall_name="Blue", hall_rows=10, hall_seats_in_row=12)
    create_cinema_hall(hall_name="VIP", hall_rows=3, hall_seats_in_row=5)
    create_cinema_hall(hall_name="Cheap", hall_rows=18, hall_seats_in_row=11)
    assert list(
        CinemaHall.objects.all().values_list("name", "rows", "seats_in_row")
    ) == [("Blue", 10, 12), ("VIP", 3, 5), ("Cheap", 18, 11)]


@pytest.mark.django_db
def test_movie_session_service_create_movie_session():
    CinemaHall.objects.create(name="Blue", rows=10, seats_in_row=12)
    CinemaHall.objects.create(name="VIP", rows=3, seats_in_row=5)
    Movie.objects.create(title="Matrix", description="Matrix description")
    Movie.objects.create(title="Batman", description="Batman description")
    datetime_1 = datetime.datetime(year=2020, month=11, day=30, hour=10, minute=30)
    datetime_2 = datetime.datetime(year=2021, month=1, day=10, hour=15, minute=15)
    create_movie_session(movie_show_time=datetime_1, cinema_hall_id=2, movie_id=1)
    create_movie_session(movie_show_time=datetime_2, cinema_hall_id=1, movie_id=2)
    create_movie_session(movie_show_time=datetime_1, cinema_hall_id=1, movie_id=2)
    assert list(
        MovieSession.objects.all().values_list(
            "show_time__date", "cinema_hall__name", "movie__title"
        )
    ) == [
        (datetime.date(2020, 11, 30), "VIP", "Matrix"),
        (datetime.date(2021, 1, 10), "Blue", "Batman"),
        (datetime.date(2020, 11, 30), "Blue", "Batman"),
    ]


@pytest.mark.django_db
def test_movie_session_service_update_movie_session(database_data):
    show_time = datetime.datetime(2022, 11, 1, 20, 30)
    Movie.objects.create(title="Interstellar", description="Interstellar description")
    CinemaHall.objects.create(name="Orange", rows=10, seats_in_row=12)
    update_movie_session(
        session_id=1,
        show_time=show_time,
        movie_id=5,
        cinema_hall_id=4,
    )
    assert list(
        MovieSession.objects.filter(id=1).values_list(
            "show_time__date", "cinema_hall__name", "movie__title"
        )
    ) == [
        (datetime.date(2022, 11, 1), "Orange", "Interstellar"),
    ]


@pytest.mark.django_db
def test_movie_session_service_update_movie_session_show_time(database_data):
    show_time = datetime.datetime(2022, 11, 11, 20, 30)
    update_movie_session(
        session_id=2,
        show_time=show_time,
    )
    assert list(
        MovieSession.objects.filter(id=2).values_list(
            "show_time__date", "cinema_hall__name", "movie__title"
        )
    ) == [
        (datetime.date(2022, 11, 11), "Cheap", "Titanic"),
    ]


@pytest.mark.django_db
def test_movie_session_service_update_movie_session_movie(database_data):
    Movie.objects.create(title="Madagascar", description="Madagascar movie")
    update_movie_session(session_id=3, movie_id=5)
    assert list(
        MovieSession.objects.filter(id=3).values_list(
            "show_time__date", "cinema_hall__name", "movie__title"
        )
    ) == [
        (datetime.date(2021, 4, 3), "VIP", "Madagascar"),
    ]


@pytest.mark.django_db
def test_movie_session_service_update_movie_session_cinema_hall(database_data):
    CinemaHall.objects.create(name="Green", rows=10, seats_in_row=16)
    update_movie_session(session_id=4, cinema_hall_id=4)
    assert list(
        MovieSession.objects.filter(id=4).values_list(
            "show_time__date", "cinema_hall__name", "movie__title"
        )
    ) == [
        (datetime.date(2021, 4, 3), "Green", "Matrix"),
    ]


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


@pytest.mark.django_db
def test_movie_session_service_get_movie_session_by_date(database_data):
    sessions_1 = get_movies_sessions("2019-8-19")
    assert list(sessions_1.values_list("movie__title", "cinema_hall__name")) == [
        ("Matrix", "Blue")
    ]

    sessions_2 = get_movies_sessions("2021-4-3")
    assert list(sessions_2.values_list("movie__title", "cinema_hall__name")) == [
        ("The Good, the Bad and the Ugly", "VIP"),
        ("Matrix", "Cheap"),
    ]


@pytest.mark.django_db
def test_movie_session_service_get_movie_session_by_id(database_data):
    session_1 = get_movie_session_by_id(1)
    assert session_1.show_time.date() == datetime.date(2019, 8, 19)
    assert session_1.movie.title == "Matrix"
    assert session_1.cinema_hall.name == "Blue"

    session_3 = get_movie_session_by_id(3)
    assert session_3.show_time.date() == datetime.date(2021, 4, 3)
    assert session_3.movie.title == "The Good, the Bad and the Ugly"
    assert session_3.cinema_hall.name == "VIP"


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
