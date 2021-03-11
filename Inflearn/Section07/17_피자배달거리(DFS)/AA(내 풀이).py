#itertools 활용
#배달거리를 시계방향으로 돌면서 구하려고 함. 이미 배달거리를 구하는 공식이 나와 있음..

import sys
import itertools as it
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = []
    #기존 피자집 좌표리스트
    pizza = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                pizza.append((i, j))
                board[i][j] = 0
                
    for x in it.combinations(pizza, m):
        for k in range(4):
            #해당 조합 부분만 2로 바꾸기
            board[x[k][0]][x[k][1]] = 2
        #해당 조합마다 도시 최소 배달거리 구하기.
        for a in range(n):
            for b in range(n):
                if board[a][b] == 1
                    
