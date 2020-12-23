import sys
#sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())

# 약수 구하기
y = []
for i in range(1, n + 1):
    if n % i == 0:
        y.append(i)

# k번째로 작은 수 구하기
if len(y) >= k:
    print(y[k - 1])
else:
    print(-1)