import sys
sys.stdin = open('input.txt', 'r')

def DFS(x, y):
    global cnt
    #넘어가자마자 집이 발견되었음.
    cnt += 1
    #한번 방문한 곳은 0으로 만들기 -> 다시 방문하지 않도록.
    mapp[x][y] = 0
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx <= n - 1 and 0 <= yy <= n - 1 and mapp[xx][yy] == 1:
            DFS(xx, yy)
        

if __name__ == '__main__':
    n = int(input())
    mapp = [list(map(int, input())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    res = []
    #첫 DFS의 시작 좌표를 2중 for문을 돌며 1인 곳을 찾아 그것의 좌표로 시작. 
    for i in range(n):
        for j in range(n):
            if mapp[i][j] == 1:
                #1을 시작점으로 잡을 때마다, 즉 매 단지마다. cnt초기화
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)