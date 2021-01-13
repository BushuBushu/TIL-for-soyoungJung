import sys

#sys.stdin = open('input.txt', 'r')

N, m = map(int, input().split())
wl = list(map(int, input().split()))

wl.sort(reverse = True)
#print(wl)

cnt = 0

while len(wl) > 2:
    if max(wl) + min(wl) > m:
        cnt += 1
        wl.remove(max(wl))
        #print(wl)
        #print('if', cnt)
    elif max(wl) + min(wl) == m:
        cnt += 1
        wl.remove(max(wl))
        wl.remove(min(wl))
        #print(wl)
        #print('if2', cnt)
        #이부분이 굉장히 이상함, 꼭 다시 생각해보
    else:
        tmp = max(wl) + min(wl)
        #print('tmp', tmp)
        while tmp < m:
            tmp += wl.pop(-1)
            #print('tmpp', tmp)
            #print('www',wl)
        #print('if3', cnt)

#print(cnt)

#마지막 두개에 대해서만

if wl[0] + wl[1] <= m:
    cnt += 1
else:
    cnt += 2
    
print(cnt)

# 강의 풀이
#deque사용하기
#froom collections import deque
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
#p = deque(p)
cnt = 0
while p:
    # p에 마지막 한명이 남은 경우를 생각해야 함.
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        #p.popleft()
        p.pop(0)
        p.pop()
        cnt += 1
print(cnt)

#deque사용
