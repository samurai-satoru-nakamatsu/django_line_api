from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from linebot import LineBotApi

from dashboard.models import Message
from webhook.models import WebhookEventObject

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


@receiver(post_save, sender=WebhookEventObject)
def post_save_webhook(sender, instance, **kwargs):
    for event in instance.raw_data['events']:
        if event['type'] == 'message':
            user_id = event['source']['userId']
            profile = line_bot_api.get_profile(user_id)
            Message.objects.create(
                user_id=user_id,
                user_name=profile.display_name,
                picture_url=profile.picture_url,
                message=event['message']['text'],
            )
