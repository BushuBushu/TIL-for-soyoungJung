import sys
#sys.stdin = open('input.txt', 'r')
#하나의 동전에 대해 사람 1, 사람 2, 사람 3에게 나눠주며 가지를 뻗는다.

def DFS(L, p1, p2, p3):
    global minn
    #cut edge 방법 생각해보기
    if L == n:
        a = set()
        a.add(p1)
        a.add(p2)
        a.add(p3)
        if len(a) == 3:
            m = max(a) - min(a)
            if m < minn:
                minn = m
    else:
        #for문으로 하는 것이 맞는가? 혹은 이렇게 3개로 하는게 맞는가??
        DFS(L + 1, p1 + coin[L], p2, p3)
        DFS(L + 1, p1, p2 + coin[L], p3)
        DFS(L + 1, p1, p2, p3 + coin[L])        
    

if __name__ == '__main__':
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    minn = 2147000000
    DFS(0, 0, 0, 0)
    print(minn)

#강의 풀이
#백을 할 때는 해당 동전을 쓰지 않은 것으로 하고, 해당 사람의 총액에서 다시 동전금액을 빼야 함.
import sys
sys.stdin = open("input.txt", 'r')
def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            #세 사람의 금액이 모두 다르다는 것을 검증.
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        #사람이 3명이니까 3가지의 가지를 뻗는 것.
        for i in range(3):
            #코인의 L번째 있는 금액을 i번째 사람에게 주는 것.
            money[i]+=coin[L]
            DFS(L+1)
            #백을 한 상황. 48번째 코드를 취소하는 것.
            #내 풀이와는 달리 money리스트에 계속 접근을 하기 때문에 반납을 해줘야 함.
            money[i]-=coin[L]

if __name__=="__main__":
    n=int(input())
    coin=[]
    tmp=[]
    #각 사람의 금액
    money=[0]*3
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
