from django.urls import include, path
from rest_framework import routers
from participations.views import ParticipationsViewSet

router = routers.DefaultRouter()

router.register(r'', ParticipationsViewSet)

urlpatterns = [
  path("", include(router.urls)),
]