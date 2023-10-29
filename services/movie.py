from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()
    if genres_ids is not None and actors_ids is not None:
        return queryset.filter(
            genres__id__in=genres_ids
        ).filter(actors__id__in=actors_ids)
    if genres_ids is not None:
        return queryset.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        return queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None
                 ) -> QuerySet[Movie]:
    create_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids is not None:
        create_movie.genres.set(genres_ids)
    if actors_ids is not None:
        create_movie.actors.set(actors_ids)
    return create_movie
