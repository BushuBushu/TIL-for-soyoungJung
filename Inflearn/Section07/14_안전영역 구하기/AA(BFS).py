import sys
from collections import deque
#sys.stdin = open('input.txt', 'r')

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#가장 높을 수 있는 높이
maxx = max(map(max, board))
res = []
Q = deque()
for i in range(maxx):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if board[j][k] > i and ch[j][k] == 0:
                Q.append((j, k))
                cnt += 1
                ch[j][k] = 1
                while Q:
                    tmp = Q.popleft()
                    for l in range(4):
                        x = tmp[0] + dx[l]
                        y = tmp[1] + dy[l]
                        if x < 0 or x >= n or y < 0 or y >= n or board[x][y] <= i or ch[x][y] == 1:
                            continue
                        ch[x][y] = 1
                        Q.append((x, y))
    res.append(cnt)
print(max(res))
