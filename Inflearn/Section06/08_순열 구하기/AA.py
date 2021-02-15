import sys
sys.stding = open('input.txt', 'r')

def DFS(L):
    global cnt
    if L == m:
        for i in range(m):
            print(res[i], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            #해당 숫자가 res에 사용되지 않았다면
            if ch[i] == 0:
                #해당 숫자를 사용한 것으로 표시하고
                ch[i] = 1
                #첫번째 인덱스에 해당 숫자를 넣겠다.
                res[L] = i
                DFS(L + 1)
                #다시 0으로 만들어 사용되지 않은 것으로 만들어 주기. 앞 라인에서 DFS()함수를 모두 실행시켰기 때문에, 위로 back한 상태임.
                ch[i] = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    #res리스트에 해당 숫자가 이미 들어 있는지 확인하는 체크 리스트
    ch = [0] * (n + 1)
    #정답을 담는 리스트
    res = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
