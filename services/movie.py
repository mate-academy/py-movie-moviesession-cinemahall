from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list | None = None,
               actors_ids: list | None = None) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        genres = Genre.objects.filter(pk__in=genres_ids)
        movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(pk__in=actors_ids)
        movie.actors.add(*actors)

    return movie
