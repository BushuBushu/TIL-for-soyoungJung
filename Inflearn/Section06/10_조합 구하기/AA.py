import sys
sys.stdin = open('input.txt', 'r')

def DFS(L, s):
    global cnt
    #if s > n:
     #   return
    if L == m:
        cnt += 1
        for j in a:
            print(j, end = ' ')
        print()
    else:
        for i in range(s, n + 1):
            a[L] = i
            DFS(L + 1, i + 1)
        
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * m
    cnt = 0
    ch = [0] 
    DFS(0, 1)

    print(cnt)

#강의 풀이
import sys
sys.stdin = open('input.txt', 'r')
def DFS(L, s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        cnt += 1
        print()
    else:
        #가지를 누구부터 뻗는가? s부터. 즉 1부터 n까지의 수를 넣는다.
        for i in range(s, n + 1):
            res[L] = i
            #L은 하나씩 뻗어간다. i + 1은 현재 0번째 인덱스보다 1큰 숫자.
            #??i+1에는 리밋을 걸지 않는가? 어차피 i는 n까지 밖에 존재하지 않기 때문에??
            DFS(L + 1, i + 1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    #조합을 담는 리스트
    res = [0] * (n + 1)
    cnt = 0
    #DFS(res의 인덱스, 시작 숫자)
    DFS(0, 1)
    print(cnt)