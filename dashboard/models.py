from django.db import models


class Message(models.Model):
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    picture_url = models.CharField(max_length=1024, blank=True, null=True, default=None)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
