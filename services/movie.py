from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_id: list, actors_id: list) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if genres_id and actors_id:
        return Movie.objects.filter(genres__in=genres_id, actors__in=actors_id)
    elif genres_id:
        return Movie.objects.filter(genres__in=genres_id)
    elif actors_id:
        return Movie.objects.filter(actors__in=actors_id)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list | None,
        actors_ids: list | None
) -> Movie:
    new_movie = Movie.objects.create(
            title=movie_title,
            description=movie_description
        )
    if genres_ids:
        return new_movie.genres.set(genres_ids)
    if actors_ids:
        return new_movie.actors.set(actors_ids)
    return new_movie
