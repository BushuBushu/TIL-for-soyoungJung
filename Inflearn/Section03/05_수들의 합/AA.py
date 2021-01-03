N, M = map(int, input().split())

li = list(map(int, input().split()))

cnt = 0

for i in range(N + 1):
    for j in range(i + 1, N + 1):
        # i부터 j까지로 slicing한 새로운 리스트
        nli = li[i : j]
        # 새롭게 slicing된 리스트의 합이 M이면
        if sum(nli) == M:
            cnt += 1
            
print(cnt)

# 강의 풀이
# 인덱스 번호를 가르키는 두개의 변수. lt와 rt
# tot 연속 부분의 합, 초기값은 a[0], 즉 1. lt부터 rt가 가르키는 곳 전까지
# lt와 rt가 같아질 수는 있어도, lt가 rt를 넘을 순 없다. 
# 값이 m보다 작으면 rt를 더해주고 같거나 크면 lt를 빼준다.
# while문이 언제 종료 되는가? rt가 N번째 오게 되면 break해주기.
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
