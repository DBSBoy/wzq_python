#电脑下棋的线程
import threading
from gobang2.engine import Engine
from gobang2.chessboard import *
from gobang2.UserGoThread import *
import socket
import pickle
class AnotherOneGo(threading.Thread):
    def __init__(self,engine,chessmanAno):
        super(AnotherOneGo, self).__init__()
        self.engine=engine
        self.chessmanAno=chessmanAno
        self.inputStr=input
        # self.inputStr = str

    def run(self):
        host = socket.gethostname()
        gport2 = 9997  # 接受玩家二的坐标
        address2 = (host, gport2)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(address2)
        while True:

            self.chessmanAno.dowait()
            self.inputStr = pickle.loads(s.recv(1024))
            # play2 = UserGoThread()
            self.engine.parseUserInputStr(self.chessmanAno,self.inputStr)
            self.chessmanAno.doNotify()

