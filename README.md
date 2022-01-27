# ChannelsReady
快速搭建一个简易的性能监控平台

#准备工作
Django web框架
Channels：使Django支持websocket
psutil: 用于获取本地硬件信息
echarts： 用于实现各种图表的UI库


#前端页面
通过booststrap实现，它提供来很多的主题样式，可以快速的搭建一个前端页面
https://v3.bootcss.com/css/
拿到的前端页面，删减完的一个简单页面


#图表制作
https://echarts.apache.org/zh/index.html
Echarts 是一个apache开源的图表UI库，可以帮你生成各种图表。

#采集系统资源
第三方库pstil 用于获取本地硬件资源信息，CPU、内存、磁盘等信息
import psutil 
psutil.cpu_times() 
psutil.cpu_count() 
psutil.swap_memory() 
psutil.virtual_memory()

#实时获取系统资源
后端：
使用channels 来扩展django 支持websocket
配置
https://blog.csdn.net/hfdxmz_3/article/details/105854871
 前端：
通过 jquery 实现wobsocket 通信

// 建立socket连接，等待服务器“推送”数据，用回调函数更新图表
$(document).ready(function () {

    var ws_get_memory = new WebSocket('ws://127.0.0.1:8000/ws/');
    ws_get_memory.onopen = function () {

        ws_get_memory.send("我来连接了");//可以给后台发送参数
    }
    //接收到消息的回调方法
    ws_get_memory.onmessage = function (event) {
        console.log(JSON.parse(event.data)['get_memory']);//后台不间断发送数据，持续接收。
        var data = JSON.parse(event.data)
        update_mychart(data["get_cpu"])
        update_youchart(data["get_memory"])
    }
