from django.db import models

# Create your models here.
class ScannedPortsModel(models.Model):
    
    ports = models.IntegerField()
    state = models.CharField(max_length=10)