from db.models import Movie
from typing import Optional, List

def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids:Optional[List[int]] = None
) -> List[Movie]:
    if genres_ids and actors_ids:
        return list(
            Movie.objects.filter(
                genres__id__in=genres_ids,
                actors__id__in=actors_ids
            ).distinct()
        )

    elif genres_ids:
        return list(
            Movie.objects.filter(
                genres__id__in=genres_ids
            ).distinct()
        )

    elif actors_ids:
        return list(
            Movie.objects.filter(
                actors__id__in=actors_ids
            ).distinct()
        )

    else:
        return list(Movie.objects.all())

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(
        movie_title: str,
        movie_description: str,
        genres_id: Optional[List[int]] = None,
        actors_id: Optional[List[int]] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_id:
        movie.genres.set(genres_id)

    if actors_id:
        movie.actors.set(actors_id)

    return movie
