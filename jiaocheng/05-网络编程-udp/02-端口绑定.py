#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 13 Mar 2018 09:13:45 PM CST

# File Name: 02-端口绑定.py
# Description:

"""

from socket import *
#创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)
#绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
udpSocket.bind(("", 8888)) #这样的话发送的端口就固定了，不是随机了，当然bind一般是接收端
udpSocket.sendto("haha", ("192.168.119.210", 2426))
