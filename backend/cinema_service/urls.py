from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path(
        "",
        serve,
        {"path": "index.html", "document_root": settings.FRONTEND_DIST},
        name="frontend",
    ),
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("api/user/", include("user.urls", namespace="user")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/doc/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Local task setup: Vue's compiled scripts, styles and public icons.
urlpatterns += static(
    "/assets/", document_root=settings.FRONTEND_DIST / "assets"
)
urlpatterns += [
    path(
        "favicon.ico",
        serve,
        {"path": "favicon.ico", "document_root": settings.FRONTEND_DIST},
    ),
]
