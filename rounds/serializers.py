from rest_framework import serializers
from rounds.models import Round

class RoundSerializer(serializers.ModelSerializer):
  class Meta:
    model = Round
    fields = [
      'id',
      'competition_id',
      'name',
      'final_date'
    ]
