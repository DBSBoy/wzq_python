#电脑下棋的线程
import threading
from gobang2.engine import Engine
from gobang2.chessboard import *
import socket
import pickle
from gobang2.UserGoThread import *
class AnotherOneGo(threading.Thread):
    def __init__(self,engine,chessmanAno):
        super(AnotherOneGo, self).__init__()
        self.engine=engine
        self.chessmanAno=chessmanAno
        self.inputStr =''

    def run(self):
        host = socket.gethostname()
        gport2 = 9998  # 接受玩家二的坐标
        address2 = (host, gport2)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(address2)
        while True:

            self.chessmanAno.dowait()
            self.inputStr = pickle.loads(s.recv(1024))
            # play2=UserGoThread()
            inputStr=self.inputStr
            self.engine.parseUserInputStr(self.chessmanAno, inputStr)

            self.chessmanAno.doNotify()

