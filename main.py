import init_django_orm  # noqa: F401
from db.models import Genre, Movie, MovieSession

genre = MovieSession.objects.get(
    id=1
)
print(genre)