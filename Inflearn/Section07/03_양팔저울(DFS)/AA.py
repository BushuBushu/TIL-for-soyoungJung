import sys
#sys.stdin = open('input.txt', 'r')
#추의 조합으로(덧셈/뺄셈 조합) 물의 무게를 구하기.
#같은 추를 중복해서 사용할 수 x

#총 세 갈래로 나뉜다.(왼쪽-오른쪽-미사용)
#추를 저울의 왼쪽에 놓으면, 추의 무게를 plus. 반대는 minus.
#모든 트리를 그려보면 잴 수 있는 무게는 플러스와 마이너스 모두 대칭적으로 나오게 됨. 따라서 중복을 피한다.

#L: w리스트를 접근하는 인덱스.
def DFS(L, s):
    global cnt
    if L == k:
        #해당 무게가 이미 나오지 않았고, 음수가 아니라면.! --> set()으로 디벨롭 시키기 가능.
        if ch[s] == 0 and s > 0:
            ch[s] = 1
            cnt += 1
        
    else:
        #추를 왼쪽에 놓기
        DFS(L + 1, s + w[L])
        #추를 오른쪽에 놓기
        DFS(L + 1, s - w[L])
        DFS(L + 1, s)
            

if __name__ == '__main__':
    k = int(input())
    #추의 무게
    w = list(map(int, input().split()))
    ssum = sum(w) 
    x = list(range(1, ssum + 1))
    #양수든 음수든 해당 수가 나왔으면 체크한다.
    ch = [0] * (ssum + 1)
    #cnt에는 구할 수 있는 모든 물의 무게 수를 저장한다.
    cnt = 0
    DFS(0, 0)
    #총 합에서 cnt를 빼면 구할 수 없는 무게 수가 나온다.
    print(ssum - cnt)

#강의 풀이
#양수/음수가 대칭적으로 생기는 것과 중복적으로 생길 수 있는 무게를 set()으로 해결하였다.
#set은 해쉬기반으로 만들어진 자료구조라 검색이 list보다 훨씬 좋습니다. 

import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    G=list(map(int, input().split()))
    s=sum(G)
    res=set()
    DFS(0, 0)
    print(s-len(res))