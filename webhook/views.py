import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# YOUR_CHANNEL_ACCESS_TOKEN
from webhook.models import WebhookEventObject

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
# YOUR_CHANNEL_SECRET
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def webhook(request):
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.body.decode('utf-8')

    # handle webhook body
    try:
        handler.handle(body, signature)
        WebhookEventObject.objects.create(raw_data=json.loads(body))
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        return HttpResponseForbidden()

    return HttpResponse('OK')


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
