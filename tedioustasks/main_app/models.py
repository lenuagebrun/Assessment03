from django.db import models

class Task(models.Model):
  description = models.CharField(max_length=100)
  time = models.IntegerField()
  person = models.CharField(max_length=80)
  
  def __str__(self):
    return self.description + ' ' + self.time + ' ' + self.person
