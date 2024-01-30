from django.db.models import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> QuerySet | Movie:
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        return queryset.filter(genres__in=genres_ids, actors__in=actors_ids)
    elif genres_ids:
        return queryset.filter(genres__in=genres_ids)
    elif actors_ids:
        return queryset.filter(actors__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> QuerySet:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.add(*Genre.objects.filter(id__in=genres_ids))

    if actors_ids:
        movie.actors.add(*Actor.objects.filter(id__in=actors_ids))

    return movie
