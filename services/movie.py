from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list = None,
               actors_ids: list = None) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    return_movie = Movie.objects.all()
    if genres_ids and actors_ids:
        return_movie = return_movie.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids).distinct()
    if genres_ids:
        return_movie = return_movie.filter(genres__id__in=genres_ids)
    if actors_ids:
        return_movie = return_movie.filter(actors__id__in=actors_ids)

    return return_movie


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list = None, actors_ids: list = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    movie.save()

    #  нельзя передавать в .create(), так как
    #  ManyToManyField добавляется отдельно через .set()
    #  сначала создать и сохранить а потом добавить ManyToManyField
    if genres_ids:
        movie.genres.set(genres_ids)  # type: ignore
    if actors_ids:
        movie.actors.set(actors_ids)  # type: ignore

    return movie
