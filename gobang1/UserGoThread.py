#用户下棋的线程
import threading
from gobang2.chessman import ChessMan
from gobang2.engine import Engine
from gobang2.chessboard import ChessBoard
import socket
import pickle
class UserGoThread(threading.Thread):
    def __init__(self,engine,chessmanUser):
        super(UserGoThread, self).__init__()
        self.engine=engine
        self.chessmanUser = chessmanUser
        self.inputStr2 = ''
    def run(self):
        while True:
            while True:
                aa =int(input('玩家1输入行号(1-15)：'))
                if (aa <= 15 & aa >= 1):
                    break
            while True:
                b = input('玩家1输入列号(a-n):')
                if (ord(b) >= ord('a') & ord(b) <= ord('f')):
                    break
            aa = str(aa)
            inputStr =aa+','+b
            self.engine.parseUserInputStr(self.chessmanUser,inputStr)
            host = socket.gethostname()
            sport = 9998  # 发送自己的坐标
            # gport2 = 9997  # 接受玩家二的坐标
            address1=(host,sport)#发送地址
            # address2=(host,gport2)#接收地址
            serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM)
            # serversocket.listen(10)


            while True:
                data = pickle.dumps(inputStr)
                # clientsocket, addr = serversocket.accept()
                serversocket.sendto(data,address1)
                # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # s.connect((host, gport2))
                # s.bind(address2)
                # self.inputStr2 = pickle.loads(s.recv(1024))
                # print('已接受')
                # print(self.inputStr2)
                # serversocket.close()
                # s.close()
                break
            # self.chessmanUser.doNotify()
            # self.chessmanUser.dowait()
            self.chessmanUser.doNotify()
            self.chessmanUser.dowait()


