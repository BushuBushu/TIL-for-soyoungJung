import sys
#sys.stdin = open("input.txt", 'r')

n = int(input())
cube =[list(map(int, input().split())) for _ in range(n)]

app = 0
#중간 행을 기점으로 양끝부터 슬라이싱하기
for i in range(n//2):
    app += sum(cube[i][n//2 - i : n - n//2 + i])
    app += sum(cube[n-1-i][n//2 - i : n - n//2 + i])
    
#중간 행 더하기
app += sum(cube[n//2])

print(app)

#강의 풀이
n = int(input())
cube =[list(map(int, input().split())) for _ in range(n)]
res = 0
#인덱스의 시작과 끝을 설정
# 첫 설정은 n의 중간값인 2의 몫으로
s = e = n // 2
for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1