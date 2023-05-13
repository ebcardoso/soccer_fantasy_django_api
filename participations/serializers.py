from rest_framework import serializers
from participations.models import Participations

class ParticipationsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Participations
    fields = [
      'id',
      'is_admin',
      'user_id',
      'league_id',
    ]
