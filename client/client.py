#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys
import json


class MsgSender:
    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "139.224.237.176"
    port = 10000

    # 连接服务，指定主机和端口
    def __init__(self):
        self.s.connect((self.host, self.port))

    def __del__(self):
        self.s.close()

    def send_QRCODE(self, content):
        send_msg = json.dumps({'type': 'QRCODE', 'content': content})
        self.s.sendall(send_msg.encode('utf-8'))


if __name__ == '__main__':
    content = "Hello, world!"
    msg_sender = MsgSender()
    msg_sender.send_QRCODE(content)
    msg_sender
    # 接收小于 1024 字节的数据
