from django.db.models import QuerySet, Q

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    query = Q()
    if genres_ids:
        query &= Q(genres__id__in=genres_ids)
    if actors_ids:
        query &= Q(actors__id__in=actors_ids)

    return Movie.objects.filter(query)


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
        genres = Genre.objects.filter(id__in=genres_ids)
        new_movie.genres.add(*genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        new_movie.actors.add(*actors)
    return new_movie
