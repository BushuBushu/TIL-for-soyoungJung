#내 풀이
import sys
sys.stdin = open('input.txt', 'r')

def DFS(x, y):
    if d[x][y] != 0:
        return DFS(x, y)
    if x == 0:
        d[x][y] = stones[x][y] + d[x][y - 1]
        DFS(x, y - 1)
    elif y == 0:
        d[x][y] = stones[x][y] + d[x - 1][y]
        DFS(x - 1, y)
        
    elif stones[x - 1][y] > stones[x][y - 1]:
        d[x][y] = stones[x][y] + d[x][y - 1]
        DFS(x, y - 1)
    elif stones[x - 1][y] < stones[x][y - 1]:
        d[x][y] = stones[x][y] + d[x - 1][y]
        DFS(x - 1, y)

if __name__ == '__main__':
    n = int(input())
    stones = [list(map(int, input().split())) for _ in range(n)]
    d = [[0] * n for _ in range(n)]
    
    
    DFS(n - 1, n - 1)
    print(d[n - 1][n - 1])

#강의 풀이
import sys
sys.stdin = open('input.txt', 'r')

def DFS(x, y):
    #memoizatioin 활용
    if d[x][y] != 0:
        return d[x][y]
    
    if x == 0 and y == 0:
        d[x][y] = stones[x][y]
        return d[x][y]
    elif x == 0:
        d[x][y] = stones[x][y] + DFS(x, y - 1)
    elif y == 0:
        d[x][y] = stones[x][y] + d[x - 1][y]
    else:
        d[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + stones[x][y]
    return d[x][y]

if __name__ == '__main__':
    n = int(input())
    stones = [list(map(int, input().split())) for _ in range(n)]
    d = [[0] * n for _ in range(n)]
    print(DFS(n - 1, n - 1))
