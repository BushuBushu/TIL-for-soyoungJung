import sys
sys.stdin = open('input.txt', 'r')

#n은 사용한 동전의 갯수, 동전의 합
def DFS(n, s):
    global res
    #cut edge tech!!!
    #트리의 레벨이 구한 res보다 커지게 되면, 더이상 뻗지 않는다.
    if n > res:
        return
    #합이 m을 넘어가면 더이상 가지를 뻗지 않는다. 
    if s > m:
        return
    #같다면, res값을 n으로 바꾸기.
    if s == m:
        if n < res:
            res = n
    else:
        #s+i 이해하기! back했을때 s는 다시 0이 된다.
        for i in a:
            print(n, s)
            DFS(n + 1, s + i)
    

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    #최소의 값을 찾는 것이기 때문에 최대값을 설정.
    res = 1247000000
    #큰 수부터 더하는 것이 시간을 더 줄일 수 있음.
    a.sort(reverse = True)
    DFS(0, 0)
    print(res)