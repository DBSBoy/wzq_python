
from gobang2.chessboard import ChessBoard

import random

from gobang2.chessman import ChessMan


class Engine:

    # 初始化 需要把棋盘对象导入
    def __init__(self, chessboard):
        self.__chessboard = chessboard

    # 计算机下棋的策略
    # 传入chessman对象的时候，已经把棋子的颜色写入
    # 此方法只需要负责填写棋子的位置
    def computerGo(self, chessman):
        if not isinstance(chessman, ChessMan):
            raise Exception('类型不对')
        # posX和posY需要在1-15之间随机生成一个数
        while True:
            posX = random.randint(1, ChessBoard.BOARD_SIZE)  # 1-15
            posY = random.randint(1, ChessBoard.BOARD_SIZE)
            if  self.__chessboard.isEmpty([posX, posY]):
                print('电脑下棋的位置：%d, %d' % (posX, posY))
                chessman.setPos([posX, posY])
                # 退出while循环
                break
    # 用户在终端下棋
    def parseUserInputStr(self, chessman, inputStr):
        #判断chessman是否为棋子类的对象
        if not isinstance(chessman, ChessMan):
            raise Exception('类型不对')

        ret = inputStr.split(',')
        value1 = ret[0]
        value2 = ret[1]
        print('')
        posX = int(value1)
        posY = ord(value2) - ord('a') +1
        chessman.setPos([posX, posY])

    def isWon(self, pos, color):
        centerX = pos[0]
        centerY = pos[1]
        #从左到右
        startY = centerY - 4
        if startY < 1:
            startY = 1
        endY = centerY + 4
        if endY > ChessBoard.BOARD_SIZE:
            endY = ChessBoard.BOARD_SIZE
        count = 0  # 技术统计，有多少颗连续的棋子
        for posY in  range(startY, endY+1):
            if self.__chessboard.getChess([centerX, posY]) == color:
                count += 1
                if(count >= 5):
                    return True
            else:
                # 一旦断开 则统计计数清0
                count = 0
        # 从上到下
        startX = centerX - 4
        if startX < 1:
            startX = 1
        endX= centerX + 4
        if endX > ChessBoard.BOARD_SIZE:
            endX = ChessBoard.BOARD_SIZE
        count = 0  # 技术统计，有多少颗连续的棋子
        for posX in range(startX, endX + 1):
            if self.__chessboard.getChess([posX, centerY]) == color:
                count += 1
                if (count >= 5):
                    return True
            else:
                # 一旦断开 则统计计数清0
                count = 0
                return False;
        # 从左下到右上
        startY = centerY - 4
        startX = centerX + 4
        if startY < 1:
            startY = 1
        endY = centerY + 4
        if endY > ChessBoard.BOARD_SIZE:
            endY = ChessBoard.BOARD_SIZE
        if startX < 1:
            startX = 1
        endX= centerX - 4
        if endX > ChessBoard.BOARD_SIZE:
            endX = ChessBoard.BOARD_SIZE
        count = 0  # 技术统计，有多少颗连续的棋子
        for posX in range(startX , endX + 1):
            for posY in range(startY, endY + 1):
                if self.__chessboard.getChess([centerX, centerY]) == color:
                    count += 1
                    if (count >= 5):
                        return True
                else:
                    # 一旦断开 则统计计数清0
                    count = 0
                    return False;
        # 从左上到右下
        startY = centerY - 4
        startX = centerX - 4
        if startY < 1:
            startY = 1
        endY = centerY + 4
        if endY > ChessBoard.BOARD_SIZE:
            endY = ChessBoard.BOARD_SIZE
        if startX < 1:
            startX = 1
        endX = centerX + 4
        if endX > ChessBoard.BOARD_SIZE:
            endX = ChessBoard.BOARD_SIZE
        count = 0  # 技术统计，有多少颗连续的棋子
        for posX in range(startX, endX + 1):
            for posY in range(startY, endY + 1):
                if self.__chessboard.getChess([centerX, centerY]) == color:
                    count += 1
                    if (count >= 5):
                        return True
                else:
                    # 一旦断开 则统计计数清0
                    count = 0
                    return False;

    # 判断是否赢棋
    # 传入一个棋子对象，判断是否赢棋
    def isWonman(self, chessman):
        if not isinstance(chessman, ChessMan):
            raise Exception('类型不对')
        pos = chessman.getPos()
        color = chessman.getColor()
        return self.isWon(pos, color)

    def play(self):
        chessman1 = ChessMan()
        chessman2 = ChessMan()
        board = ChessBoard()
        engine = Engine(board)
        first = int(input("请选择下棋顺序："))
        if first == 0:
            while True:
               chessman1.setColor('o')
               self.computerGo(chessman1)
               chessman1.setColor('x')
               while True:
                   aa = int(input('第一个字符请输入输入1-15的整数：'))
                   if (aa <= 15 & aa >= 1):
                       break
               while True:
                   b = input('第二个字符请输入a-f:')
                   if (ord(b) >= ord('a') & ord(b) <= ord('f')):
                       break
               aa = str(aa)
               inputStr = aa + ',' + b
               engine.parseUserInputStr(chessman1, inputStr)
               # 把棋子放到棋盘上
               board.setChessMan(chessman1)
               # 打印棋盘
               board.printBoard()
               self.parseUserInputStr(chessman2)
