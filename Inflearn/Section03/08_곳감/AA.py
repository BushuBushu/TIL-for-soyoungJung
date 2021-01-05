import sys
sys.stdin = open("input.txt", 'r')

N = int(input())
cube = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

for i in range(M):
    r, d, t = map(int, input().split())
    #왼쪽으로 도는 경우
    if d == 0:
        tmp = cube[r - 1][t:]
        for j in range(t):
            cube[r - 1][j - t] = cube[r - 1][j]
        cube[r - 1][:t - 1] = tmp
    #오른쪽으로 도는 경우 - 어려움..
    else:
        print(r, d, t)
        tmp = cube[r - 1][t:]
        for j in range(t):
            #out of range되는 경우..?
            if j + t >= N:
                cube[r - 1][j + t - N] = cube[r - 1][j]
            else:
                cube[r - 1][j + t] = cube[r - 1][j]
        cube[r - 1][:t - 1] = tmp
            
print(cube)

#모래시계 형태 부분만 합하기
s = 0
e = n - 1
summ = 0
for i in range(n):
    for j in range(s, e + 1):
        summ += cube[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1 

            
# 강의 풀이
#왼쪽 방향 풀이
#pop을 하고, (앞으로 당겨주고) pop으로 return된 값을 append하기
if d == 0:
    for _ in range(t):
        cube[r-1].append(a[r-1].pop(0))
#오른쪽 방향 풀이
#젤 뒤에 자료(pop())를 꺼내서 맨 앞으로 넣기. 앞에다 넣는 insert함수 사용
else:
    for _ in range(t):
        cube[r-1].insert(0, cube[r-1].pop())

#모래 시곟 