
def DFS(x):
    #0이 아니라는 것은, 이미 해당 숫자의 dfs가 돌았다는 것.
    if d[x] != 0:
        return d[x]
    if x == 0:
        return 1
    elif x == 1:
        return 2
    d[x] = DFS(x -1) + DFS(x - 2)
    return d[x]

if __name__ == '__main__':
    n = int(input())
    d = [0] * (n + 1)
    print(DFS(n))
