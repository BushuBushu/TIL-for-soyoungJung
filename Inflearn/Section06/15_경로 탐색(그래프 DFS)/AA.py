import sys
sys.stdin = open('input.txt', 'r')
'''
#ch를 어디서 해야하는지 잘 모르겠음.
def DFS(V):
    global cnt
    if V == n:
        cnt += 1
    else:
        for i in range(1, n + 1):
            ch[i] = 1
            if ch[V] == 0 and g[V][i + 1]:
                DFS(V + 1)
                ch[i] = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    chk = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
        g[b][a] = 1

print(cnt)
'''
#강의 풀이

def DFS(V):
    global cnt
    if V == n:
        cnt += 1
        for x in path:
            print(x, end = ' ' )
        print()
    else:
        for i in range(1, n + 1):
            #그래프에서 V에서 i로 가는 길이 있으면(자기 자신은 어차피 안감. 연결관계에 없기 때문) && i로 가는 길이 이미 방문돼있지 않다면
            if g[V][i] == 1 and ch[i] == 0:
                #방문 했다고 체크한 뒤
                ch[i] = 1
                path.append(i)
                #밑으로 내려가기.
                DFS(i)
                #백할 때 경로에서 삭제하기. path.pop()도 가능!!
                path.remove(i)
                #Back할 때 다시 방문 기록을 삭제하기.
                ch[i] = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    ch = [0] * (n + 1)
    path = []
    for i in range(m):
        a, b = map(int, input().split())
        #방향성이 있기 때문에 g[b][a]를 하지 않아도 된다.
        g[a][b] = 1
    #1은 무조건 방문하기 때무네
    ch[1] = 1
    #path에 1은 무조건 들어간다.
    path.append(1)
    DFS(1)

print(cnt)