from django.db.models import QuerySet

from db.models import Movie, Genre, Actor



def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet:

    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        queryset = queryset.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct()
    elif genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()

    return queryset

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(movie_title, movie_description, genres_ids=None, actors_ids=None):
    movie = Movie(
        title=movie_title,
        description=movie_description,
    )
    movie.save()

    if genres_ids:
        genre = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genre)

    if actors_ids:
        actor = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actor)

    return movie