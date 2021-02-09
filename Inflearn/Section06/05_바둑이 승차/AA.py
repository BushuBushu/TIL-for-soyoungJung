#내 풀이
import sys
sys.stdin = open('input.txt', 'r')

def DFS(idx, summ):
    maxx = -21000
    #if 문 추가. 만약 summ이 c를 넘으면.. 어떻게 하게 할까?
    #암것도 안하기?
    if idx == n:
        if summ <= c:
            if summ > maxx:
                maxx = summ

        #프린트만 하고 어떻게 최대의 값을 찾을지 방법을 못찾았음.
        print(maxx)
            
       
    else:
        DFS(idx + 1, summ + a[idx])
        DFS(idx + 1, summ)
        

if __name__ == '__main__':
    c, n = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    DFS(0, 0)

#강의 풀이
# (result를 main에 선언하고, DFS에서 global로 선언해서 사용하기
#summ이 정해진 무게보다 크다면, return해서 함수를 끝냈다. (나는 작거나 같다면 무언가 하려고 함.)
import sys
sys.stdin = open('input.txt', 'r')

def DFS(idx, summ, tsumm):
    global maxx
    #시간복잡도를 더 줄이기 위한 커트 방법 - tsum(해당 레벨에 있는 바둑이의 무게 합(포함 여부를 떠나서 해당 레벨인 바둑이 무게 모두 더하기))
    #total(바둑이들 전체 무게) - tsum = 남아있는 바둑이들의 전체 무게
    # 해당 레벨까지 더해진 summ에 위 남은 전체 무게를 더해도 maxx보다 작으면, 해당 경우의 수는 더이상 탐색 x.
    if summ + (total - tsumm) < maxx:
        return
    #if 문 추가. 만약 summ이 c를 넘으면.. 어떻게 하게 할까?
    #완전 종료시키기
    if summ > c:
        return
    if idx == n:
        if summ > maxx:
            maxx = summ
            
    else:
        DFS(idx + 1, summ + a[idx], summ + a[idx])
        DFS(idx + 1, summ, summ + a[idx])
        

if __name__ == '__main__':
    c, n = map(int, input().split())
    maxx = -2147000000
    a = [int(input()) for _ in range(n)]
    total = sum(a)
    DFS(0, 0, 0)
    print(maxx)