from django.db import models
from db.models import Genre, Movie
from django.db.models.query import QuerySet

def get_movies(genres_ids: list, actors_ids: list) -> QuerySet|None:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        # Фільтрація за жанрами І акторами
        # Використовуємо __in для "at least one genre from genres_ids"
        # та __in для "at least one actor from actors_ids"
        movies = movies.filter(genres__id__in=genres_ids, actors__id__in=actors_ids).distinct()
    elif genres_ids:
        # Фільтрація тільки за жанрами
        movies = movies.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        # Фільтрація тільки за акторами
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    # Якщо обидва списки порожні або None, повертаються всі фільми (початковий movies = Movie.objects.all())
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> Movie:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)
    return movie


