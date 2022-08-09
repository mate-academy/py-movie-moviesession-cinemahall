from db.models import Movie
from db.models import Genre
from db.models import Actor


def get_movies(genres_ids=None, actors_ids=None):
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()

    elif genres_ids is not None and actors_ids is not None:
        return Movie.objects.all().filter(
            actors__id__in=actors_ids
        ).filter(
            genres__id__in=genres_ids
        )
    elif genres_ids is not None:
        return Movie.objects.all().filter(
            genres__id__in=genres_ids
        )
    else:
        return Movie.objects.all().filter(
            actors__id__in=actors_ids
        )


def get_movie_by_id(movie_id):
    return Movie.objects.all().get(id=movie_id)


def create_movie(movie_title, movie_description,
                 genres_ids=None, actors_ids=None):
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)
