from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None) -> List[Movie]:
    qs = Movie.objects.all()
    if genres_ids and actors_ids:
        return (qs.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).distinct())
    if genres_ids:
        return qs.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        return qs.filter(actors__id__in=actors_ids).distinct()
    return qs

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids=None,
        actors_ids=None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
