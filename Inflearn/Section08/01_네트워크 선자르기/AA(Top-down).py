import sys
#sys.stdin = open('input.txt', 'r')

def DFS(x):
    if x == 1:
        d[x] = 1
        return 1
    elif x == 2:
        d[x] = 2
        return 2
    #memoization된 곳이라면 더이상 뻗지 않고 해당 값을 return한다.
    elif d[x] != 0:
        return d[x]
    else:
        d[x] = DFS(x - 1) + DFS(x - 2)
        return d[x]

if __name__ == '__main__':
    n = int(input())
    #memoizaton을 위한 리스트
    d = [0] * (n + 1)
    print(DFS(n))