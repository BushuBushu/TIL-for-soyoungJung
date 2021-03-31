def DFS(x, y):
    if y == 0:
        return x
    else:
        return DFS(y, x % y)
            
n, m = map(int, input().split())
g = DFS(n, m)
print(g)
print(n * m // g)