import socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9998
serversocket.bind((host, port))
serversocket.listen(10)
while True:
    clientsocket, addr = serversocket.accept()
    # print("连接地址: %s" % str(addr))
    # msg = '欢迎访问菜鸟教程！' + "\r\n"
    print('输入坐标：')
    msg=input()
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()