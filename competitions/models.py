from django.db import models

class Competition(models.Model):    
  name = models.CharField(max_length=255)
  type = models.IntegerField() #1-Local | 2-Regional | 3-National | 4-Internacional Club | 5-National Teams
  final_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Competitions"
