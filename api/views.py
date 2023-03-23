import hashlib
import json
import openai

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import BaseReply
from wechatpy.replies import TextReply

from .models import message_data

TOKEN = 'helloworld'
openai.api_key = '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'

@csrf_exempt
def index(request):
    if request.method == 'GET':
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echo_str = request.GET.get('echostr', '')
        try:
            check_signature(TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            echo_str = 'error'
        response = HttpResponse(echo_str, content_type="text/plain")
        return response
    else:
        msg = parse_message(request.body)
        temp000 = message_data(ToUserName=msg.source,FromUserName=msg.target,CreateTime=msg.time,MsgType=msg.type,Content=msg.content,MsgId='0',MsgDataId='0',Idx='0',Replystatus='0')
        temp000.save()

        gptmsg = [{"role": "user", "content": msg.content}]
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=gptmsg)
        
        if msg.type == 'text':
            reply = create_reply(str(completion.choices[0].message.content),msg)
        else:
            pass
        if not reply or not isinstance(reply, BaseReply):
            reply = create_reply('暂不支持您所发送的消息类型哟~ 回复“帮助”查看使用说明。', msg)
        response = HttpResponse(reply.render(), content_type="application/xml")
        return response



