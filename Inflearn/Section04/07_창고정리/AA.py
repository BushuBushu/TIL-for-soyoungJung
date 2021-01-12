import sys
#sys.stdin = open('input.txt', 'r')

#상자를 윗쪽으로 쌓는 것이 아닌 오른쪽으로 쌓기
L = int(input())
container = list(map(int, input().split()))

M = int(input())

container.sort()

#print(container)

cnt = 0
while cnt < M:#왜 M+1은 안되고 M이 되는가?
    while container[0] == min(container) and container[-1] == max(container):
        container[0] += 1
        container[-1] -= 1
        cnt += 1
        #print(container, cnt)
    container.sort()
    
#print(container)
#print(cnt)
print(max(container) - min(container))
