#끝이 2인 곳에서 역으로 올라가서 행이 0일 때 열의 값을 찾기. bottom-up방식
import sys
#sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit = 10**6

def DFS(x, y):
    if x == 0:
        print(y)
        sys.exit()
    else:
        ch[x][y] = 1
        for k in range(3):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < 10 and 0 <= yy < 10 and ch[xx][yy] == 0 and board[xx][yy] == 1:
                DFS(xx, yy)
                #ch[xx][yy] = 0

if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(10)]
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    ch = [[0] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if board[i][j] == 2 and ch[i][j] == 0:
                DFS(i, j)
                ch[i][j] = 0
                
#강의 풀이
# 위로 세 방향을 뻗는 방법을 y-1, y + 1, x - 1로 설정함.
#ch를 다시 풀 필요x. 어차피 경로는 하나이기 때문.
import sys
sys.stdin=open("input.txt", "r")
def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        #왼쪽이 0보다 작으면 board의 인덱스를 넘어가는 것.
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        #오른쪽은 10보다는 작게.
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


board=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
#행이 9인 것이 확실하기 때문에 굳이 이중 for문을 돌아 2를 찾을 필요 x.
for y in range(10):
    if board[9][y]==2:
        DFS(9, y)