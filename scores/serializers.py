from rest_framework import serializers
from scores.models import Score

class ScoreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Score
    fields = [
      'home_goals',
      'away_goals',
      'type_of_score',
      'user_id',
      'match_id',
    ]
