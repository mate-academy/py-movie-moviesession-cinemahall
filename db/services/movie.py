import init_django_orm # noqa:F401

from db.models import Genre, Actor, Movie


def get_movies(genres_ids: list[Genre] = None,
               actors_ids: list[Actor] = None):
    queryset_movies = Movie.objects.all()

    if genres_ids is not None:
        queryset_movies = queryset_movies.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset_movies = queryset_movies.filter(actors__id__in=actors_ids)

    return queryset_movies


def get_movie_by_id(movie_id: Movie):
    return Movie.objects.filter(id=movie_id)


def create_movie(movie_title,
                 movie_description,
                 genres_ids: list[Genre] = None,
                 actors_ids: list[Actor] = None):
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
