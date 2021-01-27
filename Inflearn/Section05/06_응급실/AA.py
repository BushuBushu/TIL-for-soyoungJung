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
    
#강의 풀이
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
#pos는 인덱스, val은 위험도가 됨. 튜플로 이루어진 리스트인 Q
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    # cur[1]은 위험도를 의미. Q에 존재하는 x[1]값, 즉 현재 분석 중인 환자의 위험도가 가장 높은 것이 아니라면, 뒤로 보내기
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    # 가장 높은 위험도면 치료하기
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
