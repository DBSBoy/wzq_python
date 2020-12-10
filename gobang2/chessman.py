# 棋子类
import threading
class ChessMan:
    # 棋子中有两个属性
    def __init__(self):
        self.__color = '+'
        self.__pos = [0, 0]
        self.con=threading.Condition()

    #notify封装
    def doNotify(self):
        self.con.acquire()
        self.con.notify()
        self.con.release()
    def dowait(self):
        self.con.acquire()
        self.con.wait()
        self.con.release()
    # 设置棋子的颜色
    def setColor(self, color):
        self.__color = color
    # 获取棋子的颜色

    def getColor(self):
        return self.__color

    # 设置棋子的位置
    def setPos(self, pos):
        self.__pos = pos

    # 获取棋子的位置
    def getPos(self):
        return self.__pos