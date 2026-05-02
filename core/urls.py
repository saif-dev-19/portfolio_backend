from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def health_check(request):
    return JsonResponse(
        {
            "status": "ok",
            "service": "portfolio-backend",
            "portfolio_api": "/api/portfolio/",
        }
    )


urlpatterns = [
    path("", health_check, name="health-check"),
    path("health/", health_check, name="health"),
    path("admin/", admin.site.urls),
    path("api/portfolio/", include("portfolio.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
