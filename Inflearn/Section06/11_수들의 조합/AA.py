#내 풀이
#아래와 같이 하면 중복이 허용된다. (chk를 안했기 때문? 하지만 이전 문제에서도 chk는 안했는데도 중복x.)
#nl[i + 1]을 하니까 out of index range가 뜸. 어떻게 nl의 값을 읽어올 것인가?
import sys
sys.stdin = open('input.txt', 'r')

def DFS(L, s):
    global cnt
    if L == k:
        for j in range(k):
            print(res[j], end = ' ')
        print()
        
    else:
        for i in range(n):
            res[L] = nl[i]
            DFS(L + 1, nl[i + 1])
            

if __name__ == '__main__':
    n, k = map(int, input().split())
    nl = list(map(int, input().split()))
    m = int(input())
    #조합을 담을 리스트
    res = [0] * k
    #m의 배수인 조합을 세는 변수
    cnt = 0
    #첫번째 인자: res의 인덱스.
    #두번째 인자: 시작 포인트. nl에 있는 숫자 중 다음 숫자.
    DFS(0, 0)

#강의 풀이
def DFS(L, s, summ):
    global cnt
    if L == k and summ % m == 0:
        cnt += 1
    else:
        #자료가 있는 n-1까지만 돌아야 함. index로 봤을 때. 
        for i in range(s, n):
            #i + 1이 out of range가 안되는 이유?
            DFS(L + 1, i + 1, summ + nl[i])

if __name__ == '__main__':
    n, k = map(int, input().split())
    nl = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)