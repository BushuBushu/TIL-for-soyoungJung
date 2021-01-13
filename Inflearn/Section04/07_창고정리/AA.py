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

#강의 풀이
#sort를 매 회마다 하였다. 하지만 나의 풀이는 조건문을 걸어 시간복잡도를 줄였다.

L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    a.sort()

print(a[L-1] - a[0])


#시간복잡도가 더 낮은 방법(리스트를 이용한 해쉬방법)
L=int(input())
arr=list(map(int, input().split()))
m=int(input())
cnt=[0]*101
maxH=float('-inf')
minH=float('inf')
for x in arr:
    cnt[x]+=1
    if x>maxH: maxH=x
    if x<minH: minH=x

for _ in range(m):
    if cnt[maxH]==1:
        cnt[maxH]-=1
        maxH-=1
        cnt[maxH]+=1
    else:
        cnt[maxH]-=1
        cnt[maxH-1]+=1

    if cnt[minH]==1:
        cnt[minH]-=1
        minH+=1
        cnt[minH]+=1
    else:
        cnt[minH]-=1
        cnt[minH+1]+=1
    
print(maxH-minH)