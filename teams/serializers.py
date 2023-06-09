from rest_framework import serializers
from teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = [
      'id',
      'name',
      'name_complete',
      'stadium',
      'city',
      'founded_in',
      'status',
    ]
