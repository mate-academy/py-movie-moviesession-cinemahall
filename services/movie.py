from django.db.models.query import QuerySet

from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    result_query = Movie.objects.all()

    if genres_ids and actors_ids:
        result_query = result_query.filter(genres__id__in=genres_ids)
        result_query = result_query.filter(actors__id__in=actors_ids)

    if genres_ids:
        result_query = result_query.filter(genres__id__in=genres_ids)

    if actors_ids:
        result_query = result_query.filter(actors__id__in=actors_ids)

    return result_query


def get_movie_by_id(movie_id: int) -> Movie | None:
    if not movie_id:
        print("Please enter a movie id")
        return
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        for genre_id in genres_ids:
            movie.genres.add(genre_id)

    if actors_ids:
        for actor_id in actors_ids:
            movie.actors.add(actor_id)

    return movie
