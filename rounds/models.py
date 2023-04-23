from django.db import models
from competitions.models import Competition

class Round(models.Model):    
  name = models.CharField(max_length=50)
  final_date = models.DateField()
  competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Rounds"
