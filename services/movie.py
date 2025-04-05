from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movie_sessions(
        genres_ids: list[int], /,
        actors_ids: list[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()

    if not genres_ids and not actors_ids:
        return queryset

    elif actors_ids and genres_ids:
        queryset = queryset.filter(
            genres__in=genres_ids
        ).filter(
            actors__in=actors_ids
        ).distinct()

    elif genres_ids and not actors_ids:
        queryset = queryset.filter(genres__in=genres_ids).distinct()

    elif not genres_ids and actors_ids:
        queryset = queryset.filter(actors__in=actors_ids).distinct()

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)
    return movie
