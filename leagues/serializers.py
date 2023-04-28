from rest_framework import serializers

from leagues.models import League


class LeagueSerializer(serializers.ModelSerializer):
  class Meta:
    model = League
    fields = [
      'name',
      'status',
      'competition'
    ]

