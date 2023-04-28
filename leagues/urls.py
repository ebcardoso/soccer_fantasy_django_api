from django.urls import include, path
from rest_framework import routers
from leagues.views import LeagueViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'', LeagueViewSet)

urlpatterns = [
  path("", include(router.urls)),
]