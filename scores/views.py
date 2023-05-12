from rest_framework import mixins, viewsets
from scores.models import Score
from scores.serializers import ScoreSerializer
from rest_framework.permissions import IsAuthenticated

class ScoreViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
  queryset = Score.objects.all()
  serializer_class = ScoreSerializer
  permission_classes = (IsAuthenticated,)
