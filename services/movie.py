from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None):
    all_movie = Movie.objects.all()
    if genres_ids:
        all_movie = all_movie.filter(genres__in=genres_ids)
    if actors_ids:
        all_movie = all_movie.filter(actors__in=actors_ids)
    return all_movie


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title,
                 movie_description,
                 genres_ids: list = None,
                 actors_ids: list = None
                 ):

    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description
                                 )
    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)
