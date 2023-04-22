from django.db import models
from datetime import datetime

class Competition(models.Model):    
  name = models.CharField(max_length=255)
  type = models.IntegerField() #1-Local | 2-Regional | 3-National | 4-Internacional Club | 5-National Teams
  final_date = models.DateField()
  created_at = models.DateTimeField(default=datetime.now())
  updated_at = models.DateTimeField(default=datetime.now())

  def save(self, *args, **kwargs):
    if not self.id:
      self.created_at = datetime.now()
    self.updated_at = datetime.now()
    return super(Competition, self).save(*args, **kwargs)

  def __str__(self):
    return f"{self.name} {self.type} {self.final_date}"

  class Meta:
    verbose_name_plural = "Competitions"
