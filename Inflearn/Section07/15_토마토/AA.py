# 최단 "거리를" 구하는 문제: BFS로 dis를 찾기
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
board =[list(map(int, input().split())) for _ in range(n)]
#날짜를 저장하는 배열
dis =[[0] * m for _ in range(n)]
Q = deque()
res = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            Q.append((i, j))
while Q:
    tmp = Q.popleft()
    for k in range(4):
        x = tmp[0] + dx[k]
        y = tmp[1] + dy[k]
        if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))

#토마토가 모두 있었는지 확인하는 flag
flag = 1
for i in range(n):
    for j in range(m):
        #다 돌고 만약 익지 않은 토마토가 있는 경우.
        if board[i][j] == 0:
            flag = 0

if flag == 1:
    print(max(map(max, dis)))
else:
    print(-1)
                    
print(board)