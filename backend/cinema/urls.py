from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    # Compatibility with the URLs used by the supplied frontend.
    path(
        "movies-<int:pk>/",
        MovieViewSet.as_view({"get": "retrieve"}),
        name="frontend-movie-detail",
    ),
    path(
        "movie_sessions-<int:pk>/",
        MovieSessionViewSet.as_view({"get": "retrieve"}),
        name="frontend-session-detail",
    ),
    path(
        "movies-<int:pk>-upload-image/",
        MovieViewSet.as_view(
            {"post": "upload_image"},
            **MovieViewSet.upload_image.kwargs,
        ),
        name="frontend-movie-image",
    ),
    path("", include(router.urls)),
]

app_name = "cinema"
