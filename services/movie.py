from db.models import Movie, Genre, Actor


def get_movies(genres_ids: int = None, actors_ids: int = None) -> Movie:
    movies = Movie.objects.all()
    if genres_ids and actors_ids:
        return movies.filter(genres__id__in=genres_ids,
                             actors__id__in=actors_ids).distinct()
    if genres_ids:
        return movies.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        return movies.filter(actors__id__in=actors_ids).distinct()
    return movies


def get_movie_by_id(movie_id: int) -> Movie | None:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: int = None,
                 actors_ids: int = None) -> Movie:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)
    if actors_ids:
        actors = Actor.objects.filter(pk__in=actors_ids)
        movie.actors.set(actors)
    return movie
