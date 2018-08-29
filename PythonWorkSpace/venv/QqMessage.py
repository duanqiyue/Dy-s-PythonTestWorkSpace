# encoding: utf-8
from qqbot import QQBotSlot as qqbotslot, RunBot

@qqbotslot
def onQQMessage(bot, contact, member, content):
    '''!-------识别是否是自己的话-------!'''
    if bot.isMe(contact, member)==False:
        bot.SendTo(contact, '啊？咋了？')
    if content == 'stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

if __name__ == '__main__':
	RunBot()
