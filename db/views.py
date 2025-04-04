from django.http import JsonResponse
from .models import Movie

# Представление для отображения списка всех фильмов
def movie_list(request):
    movies = Movie.objects.all()
    data = [{"title": movie.title, "description": movie.description} for movie in movies]
    return JsonResponse(data, safe=False)

# Представление для отображения конкретного фильма по ID
def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        data = {
            "title": movie.title,
            "description": movie.description,
            "actors": [actor.full_name() for actor in movie.actors.all()],
            "genres": [genre.name for genre in movie.genres.all()],
        }
        return JsonResponse(data)
    except Movie.DoesNotExist:
        return JsonResponse({"error": "Movie not found"}, status=404)