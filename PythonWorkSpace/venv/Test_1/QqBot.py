# encoding: utf-8
from qqbot import QQBotSlot as qqbotslot, RunBot
import time

#查看单词
from SelectWords import select_word
#发送消息
from QqSendMessage import sendMessageBy770
#@QQ小冰
from QqSendMessage import callXiaoBing

@qqbotslot
def onQQMessage(bot, contact, member, content):
	str = ""
	try:
		str = content.split("【")[1].split("】")[0]
	except Exception as e:
		a =1

	if str!="":
		toName = "春雷雨集团。"
		resultStr = select_word(str)
		time.sleep(0.3)
		callXiaoBing(toName)
		time.sleep(0.3)
		sendMessageBy770(resultStr,toName)
		time.sleep(0.3)


if __name__ == '__main__':
	RunBot()
