from django.contrib import admin

from webhook.models import WebhookEventObject


class WebhookEventObjectAdmin(admin.ModelAdmin):
    fields = ['id', 'created_at']


admin.site.register(WebhookEventObject, WebhookEventObjectAdmin)
