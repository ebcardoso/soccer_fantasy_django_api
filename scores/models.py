from django.db import models
from django.contrib.auth import get_user_model
from matches.models import Match

class Score(models.Model):    
  home_goals = models.IntegerField()
  away_goals = models.IntegerField()
  type_of_score = models.IntegerField(null=True)
  user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
  match_id = models.ForeignKey(Match, on_delete=models.CASCADE, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Scores"
