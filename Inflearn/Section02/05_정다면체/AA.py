n, m = map(int, input().split())
cnt = [0] * (n + m + 3)

#초기 최대값은 가장 작은 값으로!
max = -2147000000

# 눈의 합의 모든 경우의 수
for i in range(1, n + 1):
    #앞의 문제처럼 i+1부터 돌면 안됨. why? 어떤 주사위든 1이라는 눈이 나올수도 있기 때문
    for j in range(1, m + 1):
        cnt[i + j] += 1
        
#최대값 찾기 -> 이걸 max함수를 사용할 순 없나? 
for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]
        
#cnt에서 최대값을 갖고 있는 index찾기
for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end = ' ')
        
