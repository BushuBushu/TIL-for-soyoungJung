import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

info = [list(map(int, input().split())) for _ in range(7)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

minn = 2147000000
Q = deque()
#q에는 좌표의 값이 담겨야 함.
Q.append((0,0))

while True:
    #언제 break를 해야할까?
    #cnt 세는 코드는 어디에 넣어야 하나?
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        if tmp == (6, 6):
            if cnt < minn:
                minn = cnt
            break
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            #x, y가 음수가 아니거나 벽이 아니면 q에 넣기
            if x > 0 and y > 0 and info[x][y] != 1:
                Q.append((x, y))
            
# 내 풀이 2
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

info = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
ch = [[0] * 7 for _ in range(7)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#Q에는 출발점과 각 격자판과의 거리가 나온다.
Q = deque()
Q.append(0)
#Q2에는 격자판의 좌표
Q2 = deque()
Q2.append((0, 0))

while True:
    size = len(Q)
    for i in range(size):
        #이것이 바로 부모의 노드??
        tmp = Q.popleft()
        tmp2 = Q2.popleft()
        for j in range(4):
            x = tmp2[0] + dx[j]
            y = tmp2[1] + dy[j]
            #x, y가 음수가 아니거나 벽이 아니면 q에 넣기
            if x > 0 and y > 0 and info[x][y] != 1 and ch[x][y] == 0:
                ch[x][y] = 1
                Q.append(dis[x][y])
                Q2.append((x, y))
                dis[x][y] = tmp + 1
                
                
if ch[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
            
# 강의 풀이
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

info = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Q = deque()
Q.append((0, 0))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        #x, y가 음수가 아니거나 벽이 아니면 q에 넣기
        if 0 <= x <= 6 and 0 <= y <= 6 and info[x][y] == 0:
            #방문했다고 벽으로 만들기
            info[x][y] = 1
            Q.append((x, y))
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
                
                
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])

