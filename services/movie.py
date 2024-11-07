from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None, actors_ids: list[int] = None
) -> QuerySet[Movie]:
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies


def get_movie_by_id(__id: int) -> Movie:
    return Movie.objects.get(id=__id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )

    movie.genres.set(genres_ids) if genres_ids else None
    movie.actors.set(actors_ids) if actors_ids else None
