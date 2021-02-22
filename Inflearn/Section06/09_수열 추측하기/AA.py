#강의 풀이
import sys
sys.stdin=open("input.txt", "rt")
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                #각 인덱스에 해당하는 값끼리 곱해서 sum에 순차적으로 더한다.
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__ == "__main__":
    n, f=map(int, input().split())
    #주어진 수로 만들 수 있는 모든 순열을 담을 배열.
    p=[0]*n
    #이항계수를 구해서 저장할 배열. 이항계수의 양 끝은 1이기 때문에 기본 배열을 1로 설정한다.
    b=[1]*n
    #순열을 만들 때 해당 숫자가 들어갔는지 체크하는 배열
    ch=[0]*(n+1)
    # 이항계수를 만드는 방법. 인덱스 1부터 시작하는 이유: 맨 앞과 뒤는 1이기 때문. 그렇다면n-1까지만 for문을 돌아도 될까?
    # 이항계수 공식(?) 활용. 규칙 찾아내기.
    for i in range(1, n):
        b[i]=b[i-1]*(n-i)//i
    DFS(0, 0)
