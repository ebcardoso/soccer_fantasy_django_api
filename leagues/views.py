from leagues.models import League
from leagues.serializers import LeagueSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

class LeagueViewSet(viewsets.ModelViewSet):
  queryset = League.objects.all()
  serializer_class = LeagueSerializer
  permission_classes = (IsAuthenticated,)
