import init_django_orm  # noqa: F401

from db.models import Movie


def create_movie(
        movie_title: str, movie_description: str,
        genres_ids: object = None, actors_ids: object = None) -> object:
    """
    Create new movie
    """
    new_movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie


def get_movies(genres_ids: object = None, actors_ids: object = None) -> object:
    """
    Retrieve list movies by filter genres and(or) actors
    """
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> object:
    """
    Retrieve movie by movie_id
    """
    movie = Movie.objects.get(id=movie_id)

    return movie
