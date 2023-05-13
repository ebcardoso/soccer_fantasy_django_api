from django.db import models
from django.contrib.auth import get_user_model
from leagues.models import League

class Participations(models.Model):    
  is_admin = models.BooleanField(default=False)
  user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
  league_id = models.ForeignKey(League, on_delete=models.CASCADE, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Participation"
