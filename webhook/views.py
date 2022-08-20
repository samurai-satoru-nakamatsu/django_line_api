from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# YOUR_CHANNEL_ACCESS_TOKEN
line_bot_api = LineBotApi('jLx15duli4nWB1v1R1Vg+3Z+UmzYffY1mO8deiUov3D4Fij/p5LkaLZS/yN4zFz7KBJ8pKqEjAHsVKeXshAnTKMRrrdoN4E2UDkoWiGy/QXvGzs0RhyjR4fSHcPOF48qqhmMmwwbXyUt47xq63WjSwdB04t89/1O/w1cDnyilFU=')
# YOUR_CHANNEL_SECRET
handler = WebhookHandler('39577d3d67d335a2f8fb857827c90922')


@csrf_exempt
def webhook(request):
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")

    return HttpResponse('OK')


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
