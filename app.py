# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('TLJcaOv30g5m7NuIwyQL9VZFO/yMvRhLE3x9dOKJEuU+AQ6/58UgRREjmkmQk18A6Rw7n/YmZuTgkM28QfQZLV5lE96CG64u5i78jDlfQwywTCS1+mpjgrQIAT59yG7zTpXbEwD+HPYf2gWohsfVaQdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('1e00ec81e2dcd53cbce5fe50f4343485') #Your Channel Secret

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

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
