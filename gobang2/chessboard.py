# 类名首字母大写，每一个单词的首字母都要大写
# 文件名全部小写，与类名一致
# 项目的所有文件放在一个目录下
import random

from gobang2.chessman import ChessMan


class ChessBoard:
    # 类属性

    BOARD_SIZE = 15  # 棋盘大小

    # 初始化

    def __init__(self):
        self.board = []
        # 棋盘下标从0~16，后续忽略第0行，第0列
        for i in range(ChessBoard.BOARD_SIZE+1):
            tmp = []  # 描述每一行
            for j in range(ChessBoard.BOARD_SIZE+1):
                tmp.append(0)  # 描述每一个点
            self.board.append(tmp)
        print('-----------------------------------\n')

    # 清空棋盘

    def initBoard(self):
        # 直接忽略第0行
        for i in range(1, ChessBoard.BOARD_SIZE+1):  # 1~15
            for j in range(1, ChessBoard.BOARD_SIZE+1):  # 1~15
                self.board[i][j] = '+'

    # 打印棋盘
    # ord() 字符转ASCII码
    # chr() ASCII码转字符
    # 解决ACSII不能直接做算数运算
    def printBoard(self):
        print('  ', end= '')
        # 打印列号
        for i in range(1, ChessBoard.BOARD_SIZE):
            c = chr(ord('a')-1+i)
            print(c, end='')
        print()
        # 打印行号和棋盘
        for i in range(1, ChessBoard.BOARD_SIZE+1):  # 1~15
            # 打印行号
            print('%2d' % i, end='')

            for j in range(1, ChessBoard.BOARD_SIZE+1):  # 1~15

                print(self.board[i][j], end='')
            print() # 换行

        # 放置棋子
        # 参数1  坐标，棋子的位置
        # 参数2  颜色 x或o
    def setChess(self, pos, color):
        x = pos[0]
        y = pos[1]
        self.board[x][y] = color

    # 放置棋子，把棋子对象放置在棋盘上
    def setChessMan(self, chessman):
        if not isinstance(chessman, ChessMan):
            raise Exception('类型不对')
        pos = chessman.getPos()
        color = chessman.getColor()
        self.setChess(pos, color)

    # 读取棋子的颜色

    def getChess(self, pos):
        x = pos[0]
        y = pos[1]
        return self.board[x][y]

    # 判断坐标是否为空
    def isEmpty(self, pos):
        color = self.getChess(pos)
        if color == '+':
            return True
        return False


