from rounds.models import Round
from rounds.serializers import RoundSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class RoundViewSet(viewsets.ModelViewSet):
  queryset = Round.objects.all()
  serializer_class = RoundSerializer
  permission_classes = (IsAuthenticated,)
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['competition_id']

