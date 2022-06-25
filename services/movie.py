from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None):
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title, movie_description,
                 genres_ids=None, actors_ids=None):
    film = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids is not None:
        film.genres.add(*genres_ids)
    if actors_ids is not None:
        film.actors.add(*actors_ids)
