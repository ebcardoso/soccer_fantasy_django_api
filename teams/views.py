from teams.serializers import TeamSerializer
from teams.models import Team
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer
  permission_classes = (IsAuthenticated,)
  filter_backends = [SearchFilter]
  search_fields = ['$name', '$name_complete', '$stadium']
