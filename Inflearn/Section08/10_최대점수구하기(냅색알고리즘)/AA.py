import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
d = [0] * (m + 1)

for i in range(n):
    score, time = map(int, input().split())
    # m부터 time까지 탐색하도록.
    for j in range(m, time - 1, -1):
        d[j] = max(d[j], d[j - time] + score)

print(d[m])