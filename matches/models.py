from django.db import models
from teams.models import Team
from rounds.models import Round

class Match(models.Model):    
  home_goals = models.IntegerField(default=0)
  away_goals = models.IntegerField(default=0)
  match_date = models.DateTimeField()
  round_id = models.ForeignKey(Round, on_delete=models.CASCADE, null=True)
  home_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
  away_team_id = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Matches"
