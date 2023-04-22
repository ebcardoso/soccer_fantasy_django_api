from django.urls import include, path
from rest_framework import routers

from competitions.views import CompetitionViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', CompetitionViewSet)

urlpatterns = [
  path("", include(router.urls)),
]