from django.urls import include, path
from rest_framework import routers
from leagues.views import LeagueViewSet

router = routers.DefaultRouter()

router.register(r'leagues', LeagueViewSet)

urlpatterns = [
  path("", include(router.urls)),
]