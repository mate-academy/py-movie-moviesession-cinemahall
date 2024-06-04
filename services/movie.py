import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet | Movie:

    if not genres_ids and not actors_ids:
        print("inside not (genres and actors)")
        return Movie.objects.all()

    if genres_ids and actors_ids:
        print("inside genres and actors")
        return Movie.objects.filter(
            genres__id__in=genres_ids
        ).filter(actors__id__in=actors_ids)

    if genres_ids and not actors_ids:
        print("inside genres without actors")
        return Movie.objects.filter(genres__id__in=genres_ids)

    if actors_ids and not genres_ids:
        print("actors without genres")
        return Movie.objects.filter(actors__id__in=actors_ids)


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
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
