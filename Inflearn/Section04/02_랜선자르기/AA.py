import sys
sys.stdin = open('input.txt', 'r')

K, N = map(int, input().split())

l = []
for _ in range(K):
    l.append(int(input()))
maxx = sum(l) / N #랜선의 최대 길이는 이것보다 무조건 작음
#이것보다 무조건 커야하는 값은 뭘까?

#몫
summ = 0
while summ != N:
    summ = 0
    for i in l:
        #리스트 각 값을 maxx로 나누면 몫이 나옴. summ은 몫의 합
        summ += i // maxx
    print('sum',summ)
    if summ != N:
        maxx -= 1


print(int(maxx))
    

#maxx의 값을 하나씩 줄여가는 것은 시간이 너무 오래 걸림.. 
#몫을 하나 더하게 하려면?? (summ을 더하게 하려면, maxx값을 효율적으로 줄이기)
    
#강의 풀이
# 정답의 간격은 1부터 가장 긴 랜선 길이까지(처음)

# 그 길이로 만들수 있는 랜선 갯수 리턴
def Count(length):
    cnt = 0
    for x in Line:
        cnt += (x // length)
    return cnt

k, n = map(int, input().split())
Line = []
res = 0 #최댓값 찾기
largest = 0 #가장 긴 선

for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest
#이분 검색
while lt <= rt:
    mid = (lt + rt) // 2
    #답이 되냐 안되냐를 판정해주는 함수
    if Count(mid) >= n:#n보다 크더라도 정답의 후보는 됨.. why? 점차 최적의 답을 찾아간다.
        res = mid
        lt = mid + 1
    else:
        rt = mid -1

print(res)

    
     