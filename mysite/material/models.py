from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Material(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    published_date = models.DateTimeField(blank = True, null = True)
    data_url = models.TextField()
    video_url = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
