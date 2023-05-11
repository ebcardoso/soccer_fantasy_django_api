from django.db import models
from teams.models import Team
from rounds.models import Round

class Match(models.Model):    
  home_goals = models.IntegerField(default=0)
  away_goals = models.IntegerField(default=0)
  match_date = models.DateTimeField()
  round = models.ForeignKey(Round, on_delete=models.CASCADE, null=True)
  home_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
  away_team = models.IntegerField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Matches"
