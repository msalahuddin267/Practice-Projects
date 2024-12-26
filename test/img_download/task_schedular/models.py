from django.db import models

class CronJobControl(models.Model):
    is_active = models.BooleanField(default=True)
    interval = models.PositiveIntegerField(default=5)  # Interval in minutes

    def __str__(self):
        return f"Active: {self.is_active}, Interval: {self.interval} mins"

    class Meta:
        indexes = [
            models.Index(fields=["is_active", "interval"]),
        ]

    