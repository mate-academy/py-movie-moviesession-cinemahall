from django.db.models import Q, QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and not actors_ids:
        return Movie.objects.filter(
            genres__id__in=genres_ids
        )

    if actors_ids and not genres_ids:
        return Movie.objects.filter(
            actors__id__in=actors_ids
        )

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            Q(genres__id__in=genres_ids)
            & Q(actors__id__in=actors_ids)
        )


def get_movie_by_id(movie_id: int) -> Movie:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)

    return movie
