import sys
sys.stdin = open('in1.txt', 'r')

# 부분집합은 
def DFS(v):
    #DFS(4)가 되면 출력한다.
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end = ' ')
        print()
    else:
        #해당 원소가 부분집합에 들어있다.라고 체크.
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


if __name__ == '__main__':
    n = int(input())
    #해당 원소의 유무를 체크하는 리스트
    ch = [0] * (n + 1)
    DFS(1)