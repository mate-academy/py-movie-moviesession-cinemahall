from db.models import Genre


def get_genres() -> list[Genre]:
    return Genre.objects.all()


def create_genre(genre_name: str) -> Genre:
    return Genre.objects.create(name=genre_name)
