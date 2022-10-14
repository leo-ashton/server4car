from cgitb import handler
import socket
import qrcode
import json


# 1.创建一个套接字，
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.使用bind()函数将套接字与服务器地址关联
sock.bind(('0.0.0.0', 10000))   # 0.0.0.0绑定到所有的网络地址
# 3.调用listen()函数将套接字设置为服务器模式
sock.listen(50)

# 报文格式:JSON格式,具有以下字段:
# type:


class MsgHandler:
    def __init__(self):
        self.handler_dict = {'QRCODE': self.QRCODE_handler}

    def QRCODE_handler(self, msg):
        img = qrcode.make(msg['content'])
        with open("car_server/output_imgs/qrcode.png", "wb") as f:
            img.save(f)
            print("二维码已保存!")

    def handler(self, msg):
        msg = msg.decode()
        msg = json.loads(msg)
        self.handler_dict[msg['type']](msg)


if __name__ == "__main__":
    msg_handler = MsgHandler()
    while True:
        # 4.调用accept()等待客户端的消息连接
        # 如果有客户端进行连接，那么accept()函数会返回一个打开的连接与客户端地址
        connection, client_address = sock.accept()
        print("连接客户端地址：", client_address)
        while True:
            try:
                # 5.指明一个缓冲区，该缓冲区用来存放recv函数接收到的数据
                data = connection.recv(1024)
                print(data)
                if data:
                    # 6.通过sendall()进行回传客户端数据。
                    # connection.sendall("已接受到数据".encode())
                    msg_handler.handler(data)
                else:
                    print("客户端发送空信息，关闭连接")
                    connection.close()
                    break
            except Exception as e:
                print(e)
                connection.close()
        # finally:
            # 7.需要使用close()进行清理
