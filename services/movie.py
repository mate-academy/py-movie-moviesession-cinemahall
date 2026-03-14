from django.db.models import QuerySet


from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    list_movies = Movie.objects.all()
    if genres_ids:
        list_movies = list_movies.filter(genres__in=genres_ids)
    if actors_ids:
        list_movies = list_movies.filter(actors__in=actors_ids)
    return list_movies.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
