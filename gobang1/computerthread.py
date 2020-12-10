#电脑下棋的线程
import threading
from gobang2.engine import Engine
class ComputerThread(threading.Thread):
    def __init__(self,engine,chessmanPC):
        super(ComputerThread, self).__init__()
        self.engine=engine
        self.chessmanPC=chessmanPC


    def run(self):
        while True:
            self.chessmanPC.dowait()
            self.engine.computerGo(self.chessmanPC)
            # self.chessmanPC.doNotify()
            # self.chessmanPC.dowait()
            self.chessmanPC.doNotify()

            #notify