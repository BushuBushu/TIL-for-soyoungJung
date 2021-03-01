#결국 모든 문제에서 풀 문제만 골라내는 부분집합 구하기.

import sys
#sys.stdin = open('input.txt', 'r')

#Level, time, score
def DFS(L, t, s):
    global maxx
    if t > m:
        return
    if L == n:
        if s > maxx:
            maxx = s
    else:
        #굳이 ch배열을 만들지 않고, 더하냐 더하지 않냐로 부분집합에 포함되냐 되지 않느냐로 판단한다.
        DFS(L + 1, t + time[L] , s + score[L])
        DFS(L + 1, t, s)
            

if __name__ == '__main__':
    n, m = map(int, input().split())
    score = []
    time = []
    for _ in range(n):
        a, b = map(int, input().split())
        score.append(a)
        time.append(b)
    maxx = -214000
    DFS(0, 0, 0)
    print(maxx)
