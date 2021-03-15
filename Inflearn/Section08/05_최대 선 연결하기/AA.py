#결국 4번 문제와 같은 문제 - 내용만 조금 바뀜.
import sys
#sys.stdin = open('input.txt', 'r')

n = int(input())
#l = list(range(11))
r = list(map(int, input().split()))
r.insert(0, 0)
d = [0] * (n + 1)
d[1] = 1
res = 0

for i in range(2, n + 1):
    maxx = 0
    for j in range(i - 1, 0, -1):
        if r[i] > r[j] and d[j] > maxx:
            maxx = d[j]
    d[i] = maxx + 1
    
    if d[i] > res:
        res = d[i]
        
print(res)