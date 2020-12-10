import socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)
while True:
    clientsocket, addr = serversocket.accept()
    print('输入坐标：')
    msg=input()
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()