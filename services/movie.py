from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    movies = Movie.objects.all()
    if actors_ids is not None:
        movies = movies.filter(actors__id__in=actors_ids)
    if genres_ids is not None:
        movies = movies.filter(genres__id__in=genres_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        new_movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        new_movie.actors.set(actors)
