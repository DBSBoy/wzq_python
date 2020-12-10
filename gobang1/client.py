import socket
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9997
BOARD_SIZE = 15
s.connect((host, port))

test =  [([0] * 16) for i in range(16)]
data=s.recv(2048)
test=pickle.loads(data)
print('  ', end= '')
# 打印列号
for i in range(1,BOARD_SIZE+1):
    c = chr(ord('a')-1+i)
    print(c, end='')
print()
        # 打印行号和棋盘
for i in range(1, BOARD_SIZE+1):  # 1~15
            # 打印行号
    print('%2d' % i, end='')
    for j in range(1, BOARD_SIZE+1):  # 1~15
        print(test[i][j], end='')
    print() # 换行
s.close()
# print ('收到坐标为'+msg.decode('utf-8'))
