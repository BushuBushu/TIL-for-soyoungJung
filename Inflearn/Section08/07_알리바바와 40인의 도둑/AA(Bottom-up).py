import sys
#sys.stdin = open('input.txt', 'r')

n = int(input())
stones = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * n for _ in range(n)]

#d의 0행 0열 초기화
for i in range(n):
    for j in range(n):
        if i == 0:
            d[i][j] = d[i][j - 1] + stones[i][j]
        if j == 0:
            d[i][j] = d[i - 1][j] + stones[i][j]

for i in range(1, n):
    for j in range(1, n):
        #9시 방향이 더 작은 경우
        if d[i - 1][j] > d[i][j - 1]:
            d[i][j] = d[i][j - 1] + stones[i][j]
        else:
            d[i][j] = d[i - 1][j] + stones[i][j]
            

print(d[n - 1][n - 1])
