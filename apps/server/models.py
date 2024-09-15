from django.db import models
from apps.common.models import Region

class ServerAdd(models.Model):
    server_name = models.CharField(max_length=255)
    bio = models.TextField()
    server_salary = models.IntegerField()
    # lokatsiya = models.
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
