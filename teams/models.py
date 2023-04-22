from django.db import models
from datetime import datetime

class Team(models.Model):
  name = models.CharField(max_length=50)
  name_complete = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  stadium = models.CharField(max_length=100)
  founded_in = models.IntegerField()
  status = models.IntegerField(default=1)
  created_at = models.DateTimeField(default=datetime.now())
  updated_at = models.DateTimeField(default=datetime.now())

  def save(self, *args, **kwargs):
    if not self.id:
      self.created_at = datetime.now()
    self.updated_at = datetime.now()
    return super(Team, self).save(*args, **kwargs)

  class Meta:
    verbose_name_plural = "Teams"
