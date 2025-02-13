from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    if genres_ids and actors_ids:
        return (Movie.objects.filter(genres__in=genres_ids)
                .filter(actors__in=actors_ids))
    elif genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)
    else:
        return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list = None,
        genres_ids: list = None,
) -> Movie:
    movie = Movie(
        title=movie_title,
        description=movie_description,
    )
    movie.save()
    if actors_ids:
        movie.actors.add(*actors_ids)
    if genres_ids:
        movie.genres.add(*genres_ids)
    return movie
