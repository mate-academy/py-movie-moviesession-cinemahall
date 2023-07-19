from db.models import Movie, Genre, Actor
from django.db.models import QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    queryset_movies = Movie.objects.all()

    if genres_ids is not None:
        queryset_movies = queryset_movies.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset_movies = queryset_movies.filter(actors__id__in=actors_ids)

    return queryset_movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[Genre] = None,
        actors_ids: list[Actor] = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    movie.save()

    if genres_ids:
        for genre in genres_ids:
            movie.genres.add(genre)

    if actors_ids:
        for actor in actors_ids:
            movie.actors.add(actor)
