from django.urls import include, path
from rest_framework import routers
from rounds.views import RoundViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', RoundViewSet)

urlpatterns = [
  path("", include(router.urls)),
]