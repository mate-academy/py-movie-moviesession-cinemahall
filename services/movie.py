from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None,
) -> QuerySet[Movie]:
    movie = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movie

    if genres_ids:
        movie = movie.filter(genres__id__in=genres_ids)
    if actors_ids:
        movie = movie.filter(actors__id__in=actors_ids)
    return movie.distinct()


def get_movie_by_id(movie_id: Movie | None) -> dict | None:
    if movie_id:
        return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None,
) -> dict | None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
