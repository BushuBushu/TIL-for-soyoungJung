import sys
#sys.stdin = open('input.txt', 'r')
#li를 하나두고 해당 리스트의 인덱스를 DFS의 인자로 둠.

def DFS(idx):
    global cnt
    if idx == m:
        cnt += 1
        for j in li:
            print(j, end = ' ')
        print()
            
    else:
        for i in range(1, n + 1):
            li[idx] = i
            DFS(idx + 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    cnt = 0
    li = [0] * m
    DFS(0)
    print(cnt)