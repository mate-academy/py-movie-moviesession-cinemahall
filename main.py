import datetime

import init_django_orm  # noqa: F401

from services import movie, movie_session

if __name__ == '__main__':
    print(movie.get_movies([1, 2], [1]))
