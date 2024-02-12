from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    elif genres_ids and actors_ids:
        return Movie.objects.filter(
            genres_id__in=genres_ids,
            actors_id__in=actors_ids
        )
    elif genres_ids and not actors_ids:
        return Movie.objects.filter(genres_id__in=genres_ids)
    elif actors_ids and not genres_ids:
        return Movie.objects.filter(actors_id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genre_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        movie_title=movie_title,
        movie_description=movie_description,
    )
    if genre_ids:
        movie.genres.set(genre_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
