from django.db import models

class TaskFieldModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False)
