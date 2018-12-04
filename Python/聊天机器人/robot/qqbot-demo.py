from qqbot import QQBotSlot as qqbotslot, RunBot
import requests

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
        print("请求错误")
        return


@qqbotslot
def onQQMessage(bot, contact, member, content):
    # 判断不是自己发言
    if '3541356626' in str(contact) or '元素56号' in str(member):
        pass
    else:
        # 功能命令
        if content == '-hello':
            bot.SendTo(contact, '你好')
        elif content == '-stop':
            bot.SendTo(contact, 'QQ机器人已关闭')
            bot.Stop()
        else:
            # 调用图灵机器人回复
            reply = get_response(content)
            bot.SendTo(contact, reply)


if __name__ == '__main__':
    RunBot()
