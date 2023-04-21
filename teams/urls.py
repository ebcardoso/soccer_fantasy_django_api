from rest_framework.routers import DefaultRouter
from teams.views import TeamViewSet

app_name = 'teams'

router = DefaultRouter(trailing_slash=False)
router.register(r'', TeamViewSet)

urlpatterns = router.urls
