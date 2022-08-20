from django.db import models


class WebhookEventObject(models.Model):
    raw_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
