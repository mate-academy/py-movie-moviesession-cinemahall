from db.models import Movie


def get_movies(genres_ids: list = None,
               actors_ids: list = None) -> Movie:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres__in=genres_ids, actors__in=actors_ids)
    if genres_ids and not actors_ids:
        return Movie.objects.filter(
            genres__in=genres_ids)
    if not genres_ids and actors_ids:
        return Movie.objects.filter(
            actors__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    # movie  =  Movie.objects.filter(id = movie_id)
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list = None, actors_ids: list = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
