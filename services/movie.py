from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        /,
        actors_ids: list[int] = None,
)-> Movie | QuerySet:
    if genres_ids and actors_ids:
        return Movie.objects.filter(genres_id__in=genres_ids,
                                    actors_id__in=actors_ids)
    elif genres_ids:
        return Movie.objects.filter(genres_id__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors_id__in=actors_ids)

    return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie | QuerySet:
    return Movie.objects.filter(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 /,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie | QuerySet:
    movie = Movie.objects.create(title=movie_title, description=movie_description)
    if genres_ids:
        movie.genres.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
    return movie
