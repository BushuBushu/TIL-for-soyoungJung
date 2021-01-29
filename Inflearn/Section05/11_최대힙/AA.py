import sys
import heapq
#sys.stdin = open('input.txt', 'r')
heap = []

while True:
    n = int(input())

    if n == 0:
        if not heap:
            print(-1)
        else:
            a = heapq.heappop(heap)
            print(a[1])
    elif n == -1:
        break
    else:
        tn = (-n, n)
        #print(tn)
        heapq.heappush(heap, tn)

# tuple을 사용할 필요 없이, 그냥 최소힙에서 input을 음수로 바꿔주면 됨.
        