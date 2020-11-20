from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def testing_message():
    message = TextSendMessage(
        type="text",
        text="haihai~",
    )
    return message
