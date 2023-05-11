from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
  openapi.Info(
    title="Soccer Fantasy League - API",
    default_version='v1',
    description="",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="soccer@fantasy.com"),
    license=openapi.License(name="BSD License"),
   ),
  public=True,
  permission_classes=[permissions.AllowAny],
)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('teams/', include('teams.urls')),
  path('competitions/', include('competitions.urls')),
  path('rounds/', include('rounds.urls')),
  path('matches/', include('matches.urls')),
  path('leagues/', include('leagues.urls')),
]

#Djoser
urlpatterns += [
  path('api/', include('djoser.urls')),
  path('api/auth/', include('djoser.urls.authtoken')),
  path('api/auth/', include('djoser.urls.jwt')),
]

#Swagger
urlpatterns += [
  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
