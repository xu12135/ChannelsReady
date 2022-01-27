# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 3:56 PM
# @Author  : jinxu
# @File    : urls.py
from django.template.defaulttags import url
from django.urls import path, re_path
from chats.chatService import ChatService

websocket_url = [
    path("ws/", ChatService.as_asgi()),

]
