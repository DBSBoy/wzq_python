from gobang1 import chessman
from gobang2.engine import Engine
from gobang2.chessboard import *
from gobang2.UserGoThread import *
from gobang2.computerthread import *
from gobang2.AnotherOneGo import *
import struct
import pickle
import pickle
def main():
    board = ChessBoard()
    engine = Engine(board)
    engine.play()
if __name__ == '__main__':
    import socket
    board = ChessBoard()
    board.initBoard()
    engine = Engine(board)
    chessmanUser = ChessMan()
    chessmanAno = ChessMan()
    chessmanPC=ChessMan()
    chessmanAno.setColor('o')
    chessmanUser.setColor('x')

    t1 = UserGoThread(engine, chessmanUser)
    t1.start()
    t2 = AnotherOneGo(engine, chessmanAno)
    t2.start()
    # t3=ComputerThread(engine, chessmanPC)
    # t3.start()
    while True:
        chessmanUser.dowait()
        print('属于你的一轮')
        board.setChessMan(chessmanUser)
        board.printBoard()
        if engine.isWonman(chessmanUser):
            print('你赢了')
            break

        chessmanAno.doNotify()
        print('对面下棋')
        chessmanAno.dowait()
        board.setChessMan(chessmanAno)
        board.printBoard()
        if engine.isWonman(chessmanAno):
            print('对面赢啦')
            break
        chessmanUser.doNotify()
