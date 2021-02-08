import sys
#sys.stdin = open('input.txt', 'r')
#모든 부분집합의 경우의 수를 모두 내놓기.
#모든 경우의 수의 합을 total-경우의 수의 합과 같은지 비교해서 맞으면 'yes'출력하기

def DFS(i, s):
    #시간 복잡도를 더 줄인다면 추가. 밑으로 모든 인덱스로 접근하다가, 합이 total의 반을 넘어버리면, 이미 오답임.
    #나머지 모든 값을 더해도 더 작기 때문에.
    #하지만 이 조건만을 사용할 수는 없음. (s == total // 2)
    #total이 13. s // 2 == 6
    #s가 6(1, 2, 3). 인 경우 참이 안 됨. 나머지의 합은7이기 때문.
    if s > total // 2:
        return    
    #레벨끝까지 탐색을 했을 경우에, 즉, 모든 인덱스의 값까지 모두 접근했을 때.
    if i == n:
        #따져보고 출력하기
        if s == total - s:
            print('YES')
            sys.exit(0)
    else:
        #해당 원소를 포함하고, 합도 계속 더하기
        DFS(i + 1, s + a[i])
        #해당 원소를 포함하지 않고, 합도 하지 않기.
        DFS(i + 1, s)
        

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    #모든 원소의 합
    total = sum(a)
    #첫번째 인자: a리스트의 인덱스
    #두번째 인자: 경우의 수의 합
    DFS(0, 0)
    print('NO')