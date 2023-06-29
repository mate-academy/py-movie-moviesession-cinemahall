from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> list:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(genres_id__in=genres_ids,
                               actors_id_in=actors_ids)
    elif genres_ids:
        movies = movies.filter(genres_id__in=genres_ids)
    elif actors_ids:
        movies = movies.filter(actors_id__in=actors_ids)

    return list(movies)


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None):
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    return movie
