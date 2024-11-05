import init_django_orm
import services.movie
import datetime

from db.models import MovieSession
from services import cinema_hall, movie, movie_session



def main():
    name = "Matrix"
    description = "Matrix description"
    new_movie = movie.create_movie(
        movie_title=name,
        movie_description=description,
    )
    return new_movie


if __name__ == '__main__':
    print(main())