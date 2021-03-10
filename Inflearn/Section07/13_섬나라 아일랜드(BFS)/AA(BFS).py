#내 풀이 12의 BFS문제와 동일하게.. 한번 원래하던 방식으로도 해보기.
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
res = []
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 1
            board[i][j] = 0
            Q.append((i, j))
            cnt = 1
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 0:
                        continue
                    
                    board[x][y] = 0
                    Q.append((x, y))
                    cnt += 1
                #res.append(cnt)가 어떤 indentation으로 있느냐가 중요.
            res.append(cnt)
                
print(len(res))
                    
#강의 풀이 - 기존 방식이랑 똑같이
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            while Q:
                tmp=Q.popleft()
                for k in range(8):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        board[x][y]=0
                        Q.append((x, y))
            cnt+=1
print(cnt)
