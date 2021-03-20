import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
#최소값을 구하기 때문에, 넉넉하게 1000으로 잡기(최대로는 500원)
d = [1000] * (m + 1)
#0원을 거슬러주는데 0개.
d[0] = 0

#동전 하나에 대해서 먼저 쫙 돌기. 이전 문제는 하나씩 받음면서 처리 가능했음.
for i in range(n):
    for j in range(coin[i], m + 1):
        d[j] = min(d[j], d[j - coin[i]] + 1)

print(d[15])