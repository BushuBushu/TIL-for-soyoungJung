import sys
#sys.stdin = open("input.txt", 'r')

N = int(input())
cube = []


for i in range(N):
    row = list(map(int, input().split()))
    cube.append(row)

#행의 합 중 최대
#maxx = sum(max(cube)) 이게 문제인 이유??
maxx = -2147000000

#열의 합
#cs = 0 여기서 초기화 하면 안됨.
for i in range(N):
    cs = 0
    rs = 0
    for j in range(N):
        cs += cube[j][i]
        rs += cube[i][j]
    if cs > maxx:
        maxx = cs
    if rs > maxx:
        maxx = rs

#오른쪽 대각선 합
rs = 0
for x in range(N):
    rs += cube[x][x]
#if문이 for문 안에 있으면 안됨!!
if rs > maxx:
    maxx = rs

#왼쪽 대각선 합
ls = 0
for k in range(N):
    ls += cube[k][N - 1 - k]
#if문이 for문 안에 있으면 속도 느려짐. 또한 불필요함.
if ls > maxx:
    maxx = ls

print(maxx)

#강의 풀이
n = int(input())

# 함축 for문 리스트?? 고민해보기
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
#행, 열 합
for i in range(n):
    #sum을 i반복문 밑에 둔 이유? 다시 초기화 시키나?
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선 합
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)