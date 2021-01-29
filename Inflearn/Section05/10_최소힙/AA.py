import sys
#sys.stdin = open('input.txt', 'r')

import heapq

heap = []

while True:
    n = int(input())

    if n == 0:
        if not heap:
            print(-1)
        else:
            print(heapq.heappop(heap))
    elif n == -1:
        break
    else:
        heapq.heappush(heap, n)
