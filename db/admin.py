from django.contrib import admin

from .models import Movie, Actor, Genre, MovieSession, CinemaHall

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieSession)
admin.site.register(CinemaHall)
