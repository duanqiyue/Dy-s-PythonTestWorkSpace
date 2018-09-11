# -*- coding: utf-8 -*-
import QQSendMessage as qsm
import QqSendMessage_Music as qsmm


def start():
    try:
        qsmm.Message().getIp()
    except Exception as e:
        print "错误"
    finally:
        qsm.TestTK().createTk("沙雕发消息    v0.0.7")

start()


