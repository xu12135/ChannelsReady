# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 3:55 PM
# @Author  : jinxu
# @File    : chatService.py
import json
import math
import time

import psutil as psutil
from channels.generic.websocket import WebsocketConsumer


class ChatService(WebsocketConsumer):

    # 当Websocket创建连接时
    def connect(self):
        self.accept()
        print("连接建立成功")

    # 当Websocket接收到消息时
    def receive(self, text_data=None, bytes_data=None):
        print(text_data)  # 打印收到的数据
        count = 0
        while True:
            count += 1
            data = {"get_memory": memory_background_thread(count), "get_cpu": cpu_background_thread(count)}
            print(data)
            self.send(json.dumps(data))  # 对每一个WebsocketConsumer对象发送数据
            time.sleep(3)

    # 当Websocket发生断开连接时
    def disconnect(self, code):
        pass


def cpu_background_thread(count):
    time.sleep(1)
    t = time.strftime('%H:%M:%S', time.localtime())
    cpu = psutil.cpu_percent(interval=None, percpu=True)
    data = {'data': [t, cpu], 'count': count}
    return data


def memory_background_thread(count):
    time.sleep(1)
    t = time.strftime('%H:%M:%S', time.localtime())
    memory = psutil.virtual_memory()
    used_mem = math.ceil(memory.used / (1024 * 1024))
    percent_mem = memory.percent
    data = {'data': [t, used_mem], 'count': count, 'percent': percent_mem}
    return data
