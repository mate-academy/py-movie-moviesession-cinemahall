from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> None:
    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids,
                                    actors__id__in=actors_ids).distinct()
    elif genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).distinct()

    elif actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids).distinct()

    return Movie.objects.all()


def get_movie_by_id(movie_id_: int) -> Movie:
    try:
        return Movie.objects.get(id=movie_id_)
    except Movie.DoesNotExist:
        return None


def create_movie(movie_title_: str, movie_description: str,
                 actors_ids: list[int] = None,
                 genres_ids: list[int] = None) -> Movie:
    new_movie = Movie.objects.create(movie_title=movie_title_,
                                     movie_description=movie_description)
    if actors_ids:
        new_movie.actors.set(actors_ids)
    if genres_ids:
        new_movie.genres.set(genres_ids)
    return new_movie
