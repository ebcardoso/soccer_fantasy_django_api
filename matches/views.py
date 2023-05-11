from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from matches.models import Match
from matches.serializers import MatchSerializer
from rest_framework.permissions import IsAuthenticated

class MatchViewSet(viewsets.ModelViewSet):
  queryset = Match.objects.all()
  serializer_class = MatchSerializer
  permission_classes = (IsAuthenticated,)
