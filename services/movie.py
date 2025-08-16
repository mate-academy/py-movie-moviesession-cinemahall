from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list|None = None,
               actors_ids: list|None = None) -> QuerySet | None:
    if not genres_ids and not actors_ids:
            return Movie.objects.all()
    elif genres_ids and actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids,
                                    actors__id__in=actors_ids).distinct()
    elif genres_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)
    

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list|None = None,
                 actors_ids: list|None = None) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
