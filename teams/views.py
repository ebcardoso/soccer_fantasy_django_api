from teams.serializers import TeamSerializer
from teams.models import Team
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer
  permission_classes = (IsAuthenticated,)
