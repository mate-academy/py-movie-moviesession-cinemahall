from db.models import Movie


def get_movies(genres_ids, actors_ids):
    queryset = Movie.objects.all()
    if genres_ids is None and actors_ids is None:
        return queryset
    if genres_ids is not None and actors_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
        queryset = queryset.filter(actors__id__in=actors_ids)
    if genres_ids is not None and actors_ids is None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids is not None and genres_ids is None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title,
                 movie_description, genres_ids=None, actors_ids=None):
    the_movie = Movie.objects.create(title=movie_title,
                                     description=movie_description)

    if genres_ids:
        the_movie.genres.set(genres_ids)

    if actors_ids:
        the_movie.actors.set(actors_ids)

    return the_movie
