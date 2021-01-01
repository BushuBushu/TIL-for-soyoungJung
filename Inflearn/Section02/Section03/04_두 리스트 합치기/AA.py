N = int(input())
nc = list(map(int, input().split()))

M = int(input())
mc = list(map(int, input().split()))

total = nc + mc
total.sort()

for i in total:
    print(i, end = ' ')

# 강의풀이

# 내장함수를 쓰지 않고 시간복잡도를 더 좋게 풀기
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []

# 두 리스트 중 하나라도 끝나면(모두 c에 append되면) 더이상 반복문이 돌지 않음
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

# 남은 자료가 어딘지 if문으로 확인하기
# p1이 n까지 못가고 a의 자료가 남은 상태. 
if p1 < n:
    c = c + a[p1:]

# p2가 m까지 못가고 b의 자료가 남은 상태. 
if p2 < m:
    c = c + b[p2:]

for x in c:
    print(x, end = ' ')