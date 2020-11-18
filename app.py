from flask import Flask, request, abort

from message import *

import tempfile
import os
import datetime
import time

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('RzOFYxDvlUVItULXbY9yN/DvCAvlTegKgMyaIKHLma0srAQOoZGf9vEw/7AKjeQDCwEKpTR5AkNj419PcwYolQczpl/77w+1+HqqXhWZtH+CqHQ2JSMpbmkwSIt4pkCGJHGR+ZZtD3/n7LtW8/RhlgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('8aa21fcf1ab2ac11f1188620f889a31b')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# Processing messages, buat scan message terus auto reply
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '!hallo' in msg:
        message = testing_message()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        pass


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
