# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 3:51 PM
# @Author  : jinxu
# @File    : routing.py
# routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
import chats.urls
from chats.urls import websocket_url

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        chats.urls.websocket_url
    )
})