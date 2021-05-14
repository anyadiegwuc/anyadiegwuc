from django.db import models
from django.conf import settings
from django.utils import timezone

class carRace(models.Model):
    racer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    time_limti = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name