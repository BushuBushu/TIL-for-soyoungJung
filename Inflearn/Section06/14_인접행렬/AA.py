import sys
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split())
#range에서 (n)하지 않는 이유?? 인덱스 접근이 바뀌나?
g = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end = ' ')
    print()
