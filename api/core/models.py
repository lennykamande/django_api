from django.db import models
from django.conf import settings
class Points(models.Model):
    """The string given fed into the api"""
    points = models.CharField(max_length=100)
    closest_points = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.points