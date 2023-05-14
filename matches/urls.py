from django.urls import include, path
from rest_framework import routers

from matches.views import MatchViewSet

router = routers.DefaultRouter()

router.register(r'', MatchViewSet)

urlpatterns = [
  path("", include(router.urls)),
]