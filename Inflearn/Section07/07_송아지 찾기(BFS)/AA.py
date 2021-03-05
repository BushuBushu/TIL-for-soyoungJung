import sys
from collections import deque
sys.stdin=open("input.txt", "r")
MAX = 10000
#한번 방문한 좌표는 방문하지 않기 위해 체크리스트 생성.
ch = [0] * (MAX+1)
#거리 리스트. 출발점에서 몇번만에 갈 수 있는지. 인덱스는 수직선 상의 지점.
#하나의 좌표를 큐에 넣는 순간 dis도 갱신된다. why? 큐에 넣었다. = 탐색된다 = 거리가 나왔다.
dis = [0] * (MAX+1)
n,m = map(int,input().split())
#시작점은 이미 방문된 곳.
ch[n] = 1
#시작점과 시작점의 거리는 0.
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    #큐에서 나온 것이 도착지점인 경우엔 더이상 탐색할 필요 x.
    if now==m:
        break
    #next는 3가지로 이뤄진 튜플 안에서 하나씩 접근한다.
    for next in (now-1, now+1, now+5):
        #음수 좌표는 없기 때문에!
        if 0 <= next <= MAX:
            #방문한 것은 큐에 넣으면 안됨(탐색하면 안됨)
            if ch[next]==0:
                dQ.append(next)
                ch[next] = 1
                #자기 부모 값에서 1을 더한다. 왜냐, 한번움직일 때의 거리는 1이니까.
                dis[next] = dis[now]+1
                
print(dis[m])