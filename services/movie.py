from db.models import Movie


def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None):
    if not (genres_ids or actors_ids):
        return Movie.objects.all()
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genre_id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actor_id__in=actors_ids)
    return queryset

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(movie_title: str, movie_description: str, genres_ids: list[int] = None, actors_ids: list[int] = None) -> Movie:
    movie = Movie.objects.create(title=movie_title, description=movie_description)
    if genres_ids:
        movie.actors.add(*genres_ids)
    if actors_ids:
        movie.actors.add(*actors_ids)
