import sys
#sys.stdin = open('input.txt', 'r')
from collections import deque

n, k = map(int, input().split())

dq = deque(list(range(1, n + 1)))

while len(dq) > 1:
    for _ in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()
    
print(dq[0])
        
        
