from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None):
    movies = Movie.objects.all()
    if genres_ids and actors_ids:
        return movies.filter(genres_id__in=genres_ids,
                             actors_id__in=actors_ids).distinct()
    if genres_ids:
        return movies.filter(genres_id__in=genres_ids).distinct()

    if actors_ids:
        return movies.filter(actors_id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int):
    return Movie.objects.filter(id=movie_id)


def create_movie(movie_title: str, movie_description: str, genres_ids: None,
                 actors_ids: None) -> Movie:
    movie = Movie.objects.create(title=movie_title, description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
