# cyber/models.py
from django.db import models
class CyberLog(models.Model):
    log = models.TextField()
    predicted_label = models.CharField(max_length=50, null=True, blank=True)
