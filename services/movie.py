
import init_django_orm  # noqa:F401

from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None):
    movie = Movie.objects.all()
    if genres_ids:
        movie = movie.filter(genres__id__in=genres_ids)

    if actors_ids:
        movie = movie.filter(actors__id__in=actors_ids)
    return movie


def get_movie_by_id(movie_id: int):
    movie_ = Movie.objects.filter(id=movie_id).get()
    return movie_


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids=None, actors_ids=None):
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)


if __name__ == '__main__':
    pass
