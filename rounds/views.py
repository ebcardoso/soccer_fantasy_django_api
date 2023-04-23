from rounds.models import Round
from rounds.serializers import RoundSerializer
from rest_framework import mixins, permissions, viewsets

class RoundViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
  queryset = Round.objects.all()
  serializer_class = RoundSerializer

