from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet, GenreViewSet, ActorViewSet,
    CinemaHallViewSet, MovieSessionViewSet
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'halls', CinemaHallViewSet)
router.register(r'sessions', MovieSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
