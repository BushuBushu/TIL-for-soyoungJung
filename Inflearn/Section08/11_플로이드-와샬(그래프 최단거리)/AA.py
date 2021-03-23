import sys
#sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

#거리를 최대로 잡기
#dis는 i부터 j까지의 거리를 저장하는 다이나믹테이블
dis = [[5000] * (n + 1) for _ in range(n + 1)]

#자기 자신과의 거리는 0
for i in range(1, n + 1):
    dis[i][i] = 0

#아무것도 거치지 않고 직행인 경우 거리
for i in range(m):
    a, b, c = map(int, input().split())
    dis[a][b] = c

#플로이드 와샬 알고리즘.
#각 노드인 k에 대해서 2중 for문을 돌면 기존 값과 경유하는 값을 비교하는 것.
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
#5000을 M으로 바꿔주기.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dis[i][j] == 5000:
            dis[i][j] = "M"

#출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dis[i][j], end = ' ')
    print()
            

        


