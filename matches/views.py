from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from matches.models import Match
from matches.serializers import MatchSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class MatchViewSet(viewsets.ModelViewSet):
  queryset = Match.objects.all()
  serializer_class = MatchSerializer
  permission_classes = (IsAuthenticated,)
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['round_id']
