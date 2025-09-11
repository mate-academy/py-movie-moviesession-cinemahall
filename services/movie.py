from django.db.models import QuerySet

from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> Movie | QuerySet[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    if genres_ids and actors_ids:
        filtered_set = Movie.objects.filter(genres__in=genres_ids)
        filtered_set = filtered_set.filter(actors__in=actors_ids)
        return filtered_set
    if genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    if actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        for id_ in genres_ids:
            genre = Genre.objects.get(id=id_)
            movie.genres.add(genre)
    if actors_ids:
        for id_ in actors_ids:
            actor = Actor.objects.get(id=id_)
            movie.actors.add(actor)
    return movie
