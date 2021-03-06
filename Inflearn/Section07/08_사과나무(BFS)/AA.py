import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n = int(input())
ap = [list(map(int, input().split())) for _ in range(n)]

#두 리스트를 같은 인덱스 끼리 더하면, 9시-12시-3시-6시 방향으로 탐색한다.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ch = [[0] * n for _ in range(n)]
summ = 0
Q = deque()
#체크 2차원 배열의 중심(n//2)을 방문했다고 체크한다.
ch[n//2][n//2] = 1
summ += ap[n//2][n//2]
Q.append((n//2,n//2))
L = 0
while True:
    if L == n // 2:
        break
    #Q의 길이만큼 for문을 돈다. = 리드미 사진 참고.
    #하나의 노드에 대해서는 4번을 돌고, 이중for문이기 때문에 그 위는 Q의 노드만큼 돌아야 한다.
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        print(tmp)
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                summ += ap[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1
print(summ)
