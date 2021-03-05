import sys
sys.stdin = open('input.txt', 'r')

def DFS(L):
    global res
    #두자리 슬라이싱 시, 두 숫자가 26이 넘으면 탐색 중지
    #if res > '26':
        #return
    #슬라이싱 시 인덱스가 c의 범위를 넘어가면 탐색 중지
    if L > len(c) + 1:
        return
    if L == len(c) + 1:
        #print(res)
        result.append(res)
        
    else:
        #두 개의 가지로 뻗는다.(input의 현재 인덱스만 or 현재 인덱스 + 1의 값)
        res = res + c[L - 1:L]
        print(L, res)
        DFS(L + 1)
        if c[L - 2:L] < '27':  
            res = res + c[L - 2:L]
            DFS(L + 1)

if __name__ == '__main__':
    c = input()
    cnt = 0
    res = ''
    result = []
    DFS(1)
    print(result)

#강의 풀이
import sys
sys.stdin=open("input.txt", "r")
def DFS(L, P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            #문자로 바꿔주기.(A = 65)
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            #숫자를 하나씩만 비교할 때
            if code[L]==i:
                res[P]=i
                DFS(L+1, P+1)
            #숫자를 2개씩 비교.
            #code[L]과 그 다음 인덱스의 값을 10이상의 i와 비교한다. 이 때, i를 분해해서 비교한다.
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                DFS(L+2, P+1)

if __name__=="__main__":
    code=list(map(int, input()))
    n=len(code)
    #out of index range를 피하기 위해서.
    code.insert(n, -1)
    res=[0]*(n+3)
    cnt=0
    DFS(0, 0)
    print(cnt)