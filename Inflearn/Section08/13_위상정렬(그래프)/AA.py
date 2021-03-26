import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)
Q = deque()

for i in range(m):
    a, b = map(int, input().split())
    #방향 설정
    graph[a][b] = 1
    #진입차수 증가
    degree[b] += 1
    
for i in range(1, n + 1):
    if degree[i] == 0:
        Q.append(i)
        
while Q:
    x = Q.popleft()
    print(x, end = ' ')
    for i in range(1, n + 1):
        #graph를 모두 돌면서, x와 방향성이 있는 노드라면,
        if graph[x][i] == 1:
            #해당 노드의 진입차수 감소
            degree[i] -= 1
            #해당 노드가 0이 되면 Q에 append.
            if degree[i] == 0:
                Q.append(i)