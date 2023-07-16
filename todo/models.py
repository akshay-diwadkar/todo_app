from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def complete(self):
        self.is_completed = True
        self.save()

    def __str__(self):
        return self.title