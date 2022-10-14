from client import MsgSender


if __name__ == '__main__':
    sender = MsgSender()
    sender.send_QRCODE(content="Hello, world!")
    del sender
