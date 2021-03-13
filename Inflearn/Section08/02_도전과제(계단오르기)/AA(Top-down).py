import sys
sys.stdin = open('input.txt')

def DFS(x):
    if d[x] != 0:
        return d[x]
    if x == 1 or x == 2:
        return x
    d[x] = DFS(x - 1) + DFS(x - 2)
    return d[x]

if __name__ == '__main__':
    n = int(input())
    d = [0] * (n + 1)
    print(DFS(n))