import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n, m=map(int, input().split())
    dy=[0]*(m+1)
    for i in range(n):
        w, v=map(int, input().split())
        #w부터 도는 이유: j의 값이 w보다 작으면 애초에 보석을 가방에 집어넣을 수 없음.
        for j in range(w, m+1):
            dy[j]=max(dy[j], dy[j-w]+v)
    print(dy[m])
