from django.contrib import admin
from .models import Actor, Genre, Movie, CinemaHall, MovieSession

# Регистрируем модели, чтобы они отображались в админке
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(CinemaHall)
admin.site.register(MovieSession)