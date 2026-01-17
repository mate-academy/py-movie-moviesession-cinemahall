from db.models import Movie

from django.db.models import QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return queryset
    if genres_ids and actors_ids:
        return queryset.filter(genres__id__in=genres_ids).filter(actors__id__in=actors_ids)
    if genres_ids:
        return queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        return queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: Movie) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: Movie,
        movie_description: Movie,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    movie_creation = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie_creation.genres.add(*genres_ids)
    if actors_ids:
        movie_creation.actors.add(*actors_ids)
    return movie_creation
