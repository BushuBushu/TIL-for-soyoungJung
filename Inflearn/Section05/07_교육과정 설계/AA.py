import sys
#sys.stdin = open('input.txt', 'r')
from collections import deque

orr = input()
n = int(input())

for i in range(n):
    plan = input()
    order = deque(orr)
    for x in plan:
        if x in order:
            if x != order.popleft():
                print('#%d NO' % (i + 1))
                break
    # 이 else는 어디서 난거지?? for else
    else:
        #order가 비어 있다는 것은 order에 있는 필수과목이 plan에 모두 있다는 것.
        #이 조건이 없으면 앞 순서만 일부 일치해도 yes가 나옴. 필수과목을 전부 넣었는지도 파악.
        if len(order) == 0:
            print('#%d YES' % (i + 1))
        else:
            print('#%d NO' % (i + 1))
            
# 필수과목대로 설계하지 않는 모든 경우의 수를 생각해보는 것이 핵심!!








