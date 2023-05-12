from django.urls import include, path
from rest_framework import routers
from scores.views import ScoreViewSet

router = routers.DefaultRouter()

router.register(r'', ScoreViewSet)

urlpatterns = [
  path("", include(router.urls)),
]
