from db.models import Movie, Genre, Actor
from django.db.models import QuerySet


def get_movies(genres_ids: list = None,
               actors_ids: list = None) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids
        )

    if actors_ids:
        queryset = queryset.filter(
            actors__id__in=actors_ids
        )

    return queryset.distinct()


def get_movie_by_id(movie_id: Movie) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: Movie,
                 movie_description: Movie,
                 genres_ids: Genre = None,
                 actors_ids: Actor = None
                 ) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
