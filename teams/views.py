from teams.serializers import TeamSerializer
from teams.models import Team
from rest_framework import viewsets

class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer
