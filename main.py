import init_django_orm  # noqa: F401

from services import movie  # noqa: F401
from services import cinema_hall


if __name__ == "__main__":

    # print(movie.get_movies(genres_ids=[1, 2], actors_ids=[9]))
    print(movie.get_movie_by_id(1))
    # movie.create_movie("New", "some", [1, 2], [3, 4])
    # movie.del_movie_by_title("New")

    # cinema_hall.create_cinema_hall("New", 2, 10)
    # print(cinema_hall.get_cinema_halls())
    # cinema_hall.del_cinema_hall_by_title("New")
    # print(cinema_hall.get_cinema_halls())


