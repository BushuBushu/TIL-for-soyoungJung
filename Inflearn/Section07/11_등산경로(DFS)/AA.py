# 내 풀이
import sys
#sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x == mxx and y == mxy:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0
                
if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    mxi = [(i, j) for i in range(n) for j in range(n) if board[i][j] == max(map(max, board))]
    #가장 높은 구역의 x/y좌표
    mxx = mxi[0][0]
    mxy = mxi[0][1]
    #가장 낮은 구역의 x, y 좌표
    mni = [(i, j) for i in range(n) for j in range(n) if board[i][j] == min(map(min, board))]
    mnx = mni[0][1]
    mny = mni[0][1]

    cnt = 0
    ch[mnx][mny] = 1
    DFS(mnx, mny)
    #print(mnx, mny, mxx, mxy, board)
    print(cnt)

#강의 풀이
# 중복된 최대값/최소값이 있을 때 더욱 확실한 방법
import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__=="__main__":
    n=int(input())
    board=[[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-2147000000
    min=2147000000
    for i in range(n):
        tmp=list(map(int, input().split()))
        for j in range(n):
            if tmp[j]<min:
                min=tmp[j]
                sx=i
                sy=j
            if tmp[j]>max:
                max=tmp[j]
                ex=i
                ey=j      
            board[i][j]=tmp[j]
    ch[sx][sy]=1
    cnt=0
    DFS(sx, sy)
    print(cnt)