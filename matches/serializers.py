from rest_framework import serializers
from matches.models import Match

class MatchSerializer(serializers.ModelSerializer):
  class Meta:
    model = Match
    fields = [
      'id',
      'round_id',
      'match_date',
      'home_team_id',
      'away_team_id',
      'home_goals',
      'away_goals',
    ]
