from rest_framework import mixins, viewsets
from participations.models import Participations
from participations.serializers import ParticipationsSerializer
from rest_framework.permissions import IsAuthenticated

class ParticipationsViewSet(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
  queryset = Participations.objects.all()
  serializer_class = ParticipationsSerializer
  permission_classes = (IsAuthenticated,)
