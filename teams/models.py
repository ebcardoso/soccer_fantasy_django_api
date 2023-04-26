from django.db import models

class Team(models.Model):
  name = models.CharField(max_length=50)
  name_complete = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  stadium = models.CharField(max_length=100)
  founded_in = models.IntegerField()
  status = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Teams"
