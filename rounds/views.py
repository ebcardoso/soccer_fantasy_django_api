from rounds.models import Round
from rounds.serializers import RoundSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

class RoundViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
  queryset = Round.objects.all()
  serializer_class = RoundSerializer
  permission_classes = (IsAuthenticated,)

