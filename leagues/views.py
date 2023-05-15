from leagues.models import League
from leagues.serializers import LeagueSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class LeagueViewSet(viewsets.ModelViewSet):
  queryset = League.objects.all()
  serializer_class = LeagueSerializer
  permission_classes = (IsAuthenticated,)
  filter_backends = [SearchFilter]
  search_fields = ['$name']
