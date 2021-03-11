import sys
sys.stdin=open("input.txt", "r")
def DFS(L, s):
    global res
    #하나의 조합이 완성됐을 때.
    if L==m:
        #도시 피자배달거리
        sum=0
        #집 하나의 좌표에 대해서마다
        for j in range(len(hs)):
            x1=hs[j][0]
            y1=hs[j][1]
            dis=2147000000
            #피자집의 조합(한 조합 당 m가지)을 모두 검증해 최소값을 찾는다. (집 하나의 피자배달거리)
            for x in cb:
                x2=pz[x][0]
                y2=pz[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        #도시 피자배달 거리 중 최소의 값을 찾기.
        if sum<res:
            res=sum
    #조합 하나씩 만들기    
    else:
        for i in range(s, len(pz)):
            cb[L]=i
            DFS(L+1, i+1)
       
if __name__=="__main__":
    n, m=map(int, input().split())
    board=[list(map(int, input().split())) for _ in range(n)]
    #집의 좌표 저장
    hs=[]
    #피자집의 좌표 저장
    pz=[]
    #피자집 조합(len(pz) C m)을 저장할 리스트
    cb=[0]*m
    res=2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i, j))
            elif board[i][j]==2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)

