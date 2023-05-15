from competitions.models import Competition
from competitions.serializers import CompetitionSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class CompetitionViewSet(viewsets.ModelViewSet):
  queryset = Competition.objects.all()
  serializer_class = CompetitionSerializer
  permission_classes = (IsAuthenticated,)
  filter_backends = [SearchFilter]
  search_fields = ['$name']
