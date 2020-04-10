> 该项目是为了练习python操作而启动的
>
> 目前待改进的地方有：只能回复文本消息，无法回复其他类型的消息
>
> 以及有广阔空间来添加新功能

# 微信自动回复

基于网页微信和itchat模块的微信自动回复。

1. 运行脚本，登录微信后，可以对好友消息的文本消息（目前不包括群消息和其他消息）自动回复事先设置的句子。

2. 可以记录好友的消息（仅输出在终端中），不再怕消息撤回

3. 可以在好友回复指定句子之后，脚本会发邮件提醒你，且在5分钟内不再自动回复默认内容，包括禁止刷屏提醒

## 上手指南

以下指南将帮助你在本地机器上安装和运行该项目，进行开发和测试

### 安装前准备

1. 安装python3以上版本
2. 需要以前登陆过网页版的微信，若从来未登陆过网页版，则现在不能使用itchat库
3. 用```pip3 install --upgrade itchat```安装itchat，用于登录微信
4. 用```pip3 install --upgrade smtplib```安装smtplib，用于发送邮件

### 安装

下载 **WeChat_auto_reply.py** 运行

## 示例

![示例图片](https://tva1.sinaimg.cn/large/00831rSTgy1gdosegk01wj31rm0a275v.jpg)

## 贡献者

点击[contributors](https://github.com/Kinp/WeChat_autoreplay/contributors)列表查看更过贡献者

## 发起人

* **Ji Kunzhi** - *Initial work* - [Kinp](https://github.com/Kinp)

## License

暂时没有

## 参考

[itchat文档](https://itchat.readthedocs.io/zh/latest/)