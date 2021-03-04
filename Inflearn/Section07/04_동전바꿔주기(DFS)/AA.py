import sys
#sys.stdin = open('input.txt', 'r')

#하나의 동전에 대해서 동전의 갯수만큼 + 1(사용하지 않음) 가지를 뻗었다.

def DFS(L, s):
    global cnt
    if s > t:
        return
    if L == k:
        if s == t:
            cnt += 1
    else:
        for i in range(ni[L] + 1):
            DFS(L + 1, s + (pi[L] * i))
 
if __name__ == '__main__':
    t = int(input())
    k = int(input())
    pi = []
    ni = []
    for _ in range(k):
        a, b = map(int, input().split())
        pi.append(a)
        ni.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)