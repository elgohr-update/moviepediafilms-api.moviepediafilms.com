"""moviepedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    url("", include("django_prometheus.urls")),
    path("admin/", admin.site.urls),
    url(r"^api-auth/", include("rest_framework.urls")),
    url(r"^(?P<version>(v1))/", include("api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path(
            "openapi",
            get_schema_view(
                title="Moviepedia Films", description="API endpoints", version="1.0.0"
            ),
            name="openapi-schema",
        ),
        path(
            "swagger-ui/",
            TemplateView.as_view(
                template_name="swagger-ui.html",
                extra_context={"schema_url": "openapi-schema"},
            ),
            name="swagger-ui",
        ),
    ]
