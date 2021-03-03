import sys
#sys.stdin = open('input.txt', 'r')


#포함되는 날짜, 금액
def DFS(L, s):
    global maxx
    #날짜가 넘어가 버리면 그만하기.??
    if L > n + 1:
        return
    if L == n + 1:
        if s > maxx:
            maxx = s
    else:
        #해당 날짜가 포함될 때 -> sum을 더한다.
        DFS(L + time[L], s + pay[L])
        #해당 날짜가 포함되지 않으면, 다음 날짜로 옮겨가게 된다.
        DFS(L + 1, s)
        

if __name__ == '__main__':
    n = int(input())
    time = []
    pay = []
    for _ in range(n):
        a, b = map(int, input().split())
        time.append(a)
        pay.append(b)
    #해당 리스트의 인덱스를 날짜로 쓰기 위해서 index 0번째를 의미없는 0으로 insert한다.
    time.insert(0, 0)
    pay.insert(0, 0)
    maxx = -2147000000
    DFS(1, 0)
    print(maxx)