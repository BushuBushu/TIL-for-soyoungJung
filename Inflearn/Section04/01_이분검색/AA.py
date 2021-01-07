import sys
#sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
idx = N // 2
x = li[idx]
#print(li)
#print(x)

while x != M:
    if x > M:
        idx -= 1
        x = li[idx]
    elif x < M:
        idx += 1
        x = li[idx]

print(li.index(x) + 1)

# 강의 풀이
# 포인터 변수 2개 잡기(lt, rt)
# 중간 포인터 = (lt + rt) // 2
# 중간 포인트가 m과 동일하면 중간포인트를 그대로 출력하기
# 아니라면 rt값과 lt값을 조정하여(m이 크면 lt조정, 반대면 rt) 찾는 범위를 절반으로 줄여가기

a = [] #입력받은 리스트
a.sort()
lt = 0
rt = len(a) - 1
while lt <= rt: #lt가 rt보다 크거나 같으면 이분탐색을 모두 한 것이기 때문에 탐색 종료
    mid = (lt + rt) // 2
    if a[mid] == M:
        print(mid + 1)
        break
    elif a[mid] > M:
        rt = mid -1
    else:
        lt = mid + 1
