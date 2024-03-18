from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: list[int] = None, actors_ids: list[int] = None
) -> QuerySet[Movie]:
    movis = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movis
    if genres_ids and actors_ids:
        return movis.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        )
    if genres_ids:
        return movis.filter(genres__id__in=genres_ids)
    if actors_ids:
        return movis.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie
