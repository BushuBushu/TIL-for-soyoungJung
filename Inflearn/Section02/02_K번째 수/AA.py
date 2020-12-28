T = int(input())

for test in range(T):
    N, s, e, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = l[s - 1: e]
    l.sort()
    
    print('#', test + 1, l[k - 1])