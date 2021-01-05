import sys
#sys.stdin = open("input.txt", 'r')

N = int(input())
cube = [list(map(int, input().split())) for _ in range(N)]
#가장자리 0으로 초기화

cube.insert(0, [0] * (N+2))
cube.insert(N + 1, [0] * (N+2))
for i in range(1, N + 1):
    cube[i].insert(0, 0)
    cube[i].insert(N + 1, 0)

#for x in cube:
#    print(x)

cnt = 0
#상하좌우 따지기 0을 제외한 곳 따지기
for j in range(1, N + 1):
    for k in range(1, N + 1):
        #print(cube[j][k])
        if cube[j][k] > cube[j-1][k] and cube[j][k] > cube[j+1][k] and cube[j][k] > cube[j][k-1] and cube[j][k] > cube[j][k+1]:
            cnt += 1
print(cnt)

#강의 풀이
#0으로 초기화
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0 
#i번째와 j번째를 더하여서 인덱스를 상, 우, 하, 좌(시계방향으로)로 조절
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
    