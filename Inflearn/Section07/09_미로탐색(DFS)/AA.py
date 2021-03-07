import sys
# sys.stdin = open('input.txt', 'r')

#DFS인자로 cnt를 굳이 같으 넣으면 지저분해짐.
def DFS(x, y):
    global cnt
    #if L[0] < 0 or L[0] > 6 or L[1] < 0 or L[1] > 7 or board[L[0]][L[1]] == 1:
     #   return
    #어떤 조건에서 DFS를 끝내야 하는가?
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx <= 6 and 0 <= ty <= 6 and board[tx][ty] == 0:
                board[tx][ty] = 1
                DFS(tx, ty)
                board[tx][ty] = 0
                
if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(7)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    #출발 지점을 방문했다고 1로 변경.
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)