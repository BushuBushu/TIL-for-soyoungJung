import sys
#sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

def DFS(x, y, i):
    ch[x][y] = 1
    for l in range(4):
        xx = x + dx[l]
        yy = y + dy[l]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] > i and ch[xx][yy] == 0:
            DFS(xx, yy, i)

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    #cnt = 0
    res = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    #maxx = max(map(max, board))
    #print(maxx)
    #높이를 0부터 돌기
    #amxx까지만 돌아도 상관없음.
    for i in range(100):
        #이 부분에서 초기화해주기.
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for j in range(n):
            for k in range(n):
                if board[j][k] > i and ch[j][k] == 0:
                    cnt += 1
                    DFS(j, k, i)
        res = max(res, cnt)
        #cnt가 0이라는 것은 최고 높이까지 왔다는 소리.
        if cnt == 0:
            break
    print(res)