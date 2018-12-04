import requests
import itchat

KEY = '9826d3b387c9483badb65992bfbf63bc'


def get_response(msg):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
    }
    try:
        r = requests.post(api_url, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # print(msg.User)
    print(msg.User['NickName'] +msg['Text'])
    # defaultReply = 'I received: ' + msg['Text']
    reply = 'I am a Robot: ' + get_response(msg['Text'])
    print(reply)
    return reply


itchat.auto_login(hotReload=False)
itchat.run()
