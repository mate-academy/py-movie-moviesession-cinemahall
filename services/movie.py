from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None):
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id):
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title,
    movie_description,
    genres_ids=None,
    actors_ids=None
):
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
