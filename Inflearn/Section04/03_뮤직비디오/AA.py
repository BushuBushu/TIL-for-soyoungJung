import sys
sys.stdin = open('input.txt', 'r')

'''
def cntdvdnum(size):
    for i in ml:
        summ += i
        if summ

    
    
N, M = map(int, input().split())

ml = list(map(int, input().split()))

#for문을 돌면서, sum(ml) / M은 dvd의 최소 용량이다.
#최소용량으로 나눈 나머지의 값을 더한 것이 dvd용량?
#나머지값 혹은 소수점 단위를 60초로 나눈 몫
summ = 0
for i in ml:
    sum += i
minn = summ / M
'''
#가장 작을 수 있는 용량
lt = max(ml)
#가장 클 수 있는 용량
rt = sum(ml)
answer = 0

while lt >= rt:
    mid = (lt + rt) // 2
    if Size(mid) * M <= sum(ml):
        answer = mid
        rt = mid -1
    else:
        lt = mid + 1

print(answer)


# 강의풀이
def Count(capacity):
    cnt = 1#기본으로 필요한 dvd갯수
    summ = 0
    for x in Music:
        if summ + x > capacity:
            cnt += 1
            summ = x #이걸 왜 x로 초기화 하는가? 새로운 dvd에 x값을 담는 것 따라서 디비디 용량, 즉 capa는 어떤 노래보다도 크거나 같음. 이 논리를 충족시키기 위해 maxx조건을 추가함..
        else:
            summ += x
    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx = max(Music)
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    #dvd한장의 용량 = mid, n곡으 ㄹ모두 저장하려면 몇장의 dvd가 필요한지 리턴해주는 함수
    if  mid >= maxx and Count(mid) <= m:
        res = mid
        # 더 좋은 답을 향해서 가기, 용량의 최소 찾기. mid보다 큰 것은 당연히 답이 됨. 더 작은 쪽을 좁혀가
        rt = mid - 1
    else:
        lt = mid + 1#아니라면 더 작은
        
print(res)
