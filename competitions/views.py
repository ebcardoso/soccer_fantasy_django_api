from competitions.models import Competition
from competitions.serializers import CompetitionSerializer
from rest_framework import mixins, permissions, viewsets

class CompetitionViewSet(viewsets.ModelViewSet):
  queryset = Competition.objects.all()
  serializer_class = CompetitionSerializer
