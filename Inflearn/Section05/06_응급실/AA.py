import sys
#sys.stdin = open('input.txt', 'r')
from collections import deque

n, m = map(int, input().split())
dq = deque(list(map(int, input().split())))
#각 환자에 index 리스트로, 위치가 바껴도 인덱스 값을 사용할 수 있도록. dq가 옮겨질 때마다 똑같이 옮겨진다.
chkdq = deque(list(range(n)))
# 진료횟수
res = 0
            
while True:
    #환자의 위험도가 가장 큰 것이 맨 앞에 온 경우가 아니라면 계속 자리 옮기기    
    while dq[0] != max(dq):
        dq.append(dq.popleft())
        chkdq.append(chkdq.popleft())
    # 위험도가 가장 높은 것이 앞으로 왔다면 
    dq.popleft()
    if chkdq[0] == m:
        res += 1
        print(res)
        break
    else:
        chkdq.popleft()
        res += 1
    
