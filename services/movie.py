from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_id: list, actors_id: list) -> QuerySet[Movie]:
    queryset = Movie.objects.all()

    if genres_id and actors_id:
        return Movie.objects.filter(genre__in=genres_id, actor__in=actors_id)
    elif genres_id:
        return Movie.objects.filter(genre__in=genres_id)
    elif actors_id:
        return Movie.objects.filter(actor__in=actors_id)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list | None,
        actors_ids: list | None
) -> Movie:
    if genres_ids and actors_ids:
        return Movie.objects.create(
            title=movie_title,
            description=movie_description,
            genres=genres_ids,
            actors=actors_ids
        )
    elif genres_ids and not actors_ids:
        return Movie.objects.create(
            title=movie_title,
            description=movie_description,
            genres=genres_ids
        )
    elif not genres_ids and actors_ids:
        return Movie.objects.create(title=movie_title, description=movie_description, actors=actors_ids)
    else:
        return Movie.objects.create(title=movie_title, description=movie_description)
