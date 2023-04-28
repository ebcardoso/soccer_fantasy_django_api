from django.db import models
from competitions.models import Competition

class League(models.Model):    
  name = models.CharField(max_length=255)
  status = models.BooleanField(default=True)
  competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Leagues"
