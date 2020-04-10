#!/usr/bin/python3

import itchat
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 以下的常量，需要自己设置
MY_SENDER = 'XXX@163.com'  # 用于发送邮件的邮箱的账号
MY_PASS = '******'  # 用于发送邮件的邮箱的密码
MY_USER = 'XXX@qq.com'  # 用于接收邮件的邮箱
# 以下两行在电子邮箱中可以查到，大概在邮箱设置那里
SMTP_SERVER_ADDRESS = 'smtp.163.com'  # SENDER发送优秀的SMTP服务器的地址
SMTP_SERVER_PORT = 465  # SMTP服务的端口
DEFAULT_REPLY = '学习中\n在走路没看到\n吃饭去了\n我洗澡去了\n我不是故意的\n哦\n有点困了\n我先睡了\n手机没电了\n晚安！\n😊\n\n回复【有1吗】召唤'  # 默认回复消息
OTHER_REPLY = '🈶️，正在赶来的路上。\nJust a moment, please!\n\n🉑️电话/信息👇\n135****9198\n188****2808'  # 接到指定语句后回复的消息
WARNING_MESSAGE = '🙅‍♂️禁止刷消息🈲\n\n急事通电话👇\n135****9198\n188****2808'  # 警告禁止刷屏的消息
TURNING = '有1吗'  # 这里是指定语句，类似‘回复【1】获取XXX’
MAX_TIMES_TO_WARNING = 5  # 在收到指定语句后每收到多少次消息则发出警告
MAX_TIME = 300  # 恢复的时间，单位：秒。之后回复默认字段

# 若在该字典里面，则五分钟内不自动回复。键为备注，值为数组[次数, 时间]
AutoReplyDict = {'defaultKey': 'defaultValue'}


def send_email(remarkName, nickName):
    try:
        mainBody = "{}(昵称：{})发来消息了".format(remarkName, nickName)
        msg = MIMEText(mainBody, 'plain', 'utf-8')  # 设置邮件的内容
        msg['From'] = formataddr(["jkz163", MY_SENDER])  # 设置发件人的昵称
        msg['To'] = formataddr(["jkzqq", MY_USER])  # 设置收件人的昵称
        emailSubject = "【{}(昵称：{})】发消息了".format(remarkName, nickName)
        msg['Subject'] = emailSubject  # 设置邮件的主题
        server = smtplib.SMTP_SSL(SMTP_SERVER_ADDRESS,
                                  SMTP_SERVER_PORT)  # 设置邮箱SMTP的信息
        server.login(MY_SENDER, MY_PASS)  # 登录邮件
        server.sendmail(MY_SENDER, [
            MY_USER,
        ], msg.as_string())  # 发送邮件
        server.quit()  # 退出邮箱
        return True
    except Exception:
        return False


@itchat.msg_register(itchat.content.TEXT)  # 注册针对文本消息的处理函数
def text_reply(msg):
    content = msg['Text']  # 参数msg是一个字典，Text是消息内容，FromUserName是消息来源
    friend = itchat.search_friends(
        userName=msg['FromUserName'])  # 在好友列表中搜索好友，以获取好友更多信息
    nickName = friend['NickName']  # 好友的昵称
    remarkName = friend['RemarkName']  # 你给好友的备注
    print("好友:【%s（昵称：%s）】于：【%s】发来消息: 【%s】" %
          (remarkName, nickName,
           time.strftime('%Y-%m-%d %H:%M:%S',
                         time.localtime()), content))  # 在命令行中显示消息记录
    if remarkName in AutoReplyDict:  # 如果在字典里
        AutoReplyDict_Value = AutoReplyDict[remarkName]
        if content == TURNING:  # 转折点的处理
            if time.time() - AutoReplyDict_Value[1] >= MAX_TIME:  # 5min后在字典中去除
                del AutoReplyDict[remarkName]
        AutoReplyDict_Value[0] = AutoReplyDict_Value[0] + 1  # 禁止刷屏计数器
        if AutoReplyDict_Value[0] > MAX_TIMES_TO_WARNING - 1:  # 计数器每大于5次则发送提示
            AutoReplyDict_Value[0] = 0
            return WARNING_MESSAGE
        else:
            return  # 不回复
    else:
        if content == TURNING:  # 转折点的处理
            AutoReplyDict[remarkName] = [0, time.time()]  # 没在字典里则添加进去
            if send_email(remarkName, nickName):  # 发邮件通知
                return OTHER_REPLY  # 回复
            else:
                print("【错误】邮件发送失败")  # 发送邮件失败
        else:  # 默认处理
            return DEFAULT_REPLY


itchat.auto_login()
itchat.run()
