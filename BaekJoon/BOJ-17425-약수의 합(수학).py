#내 풀이 - 시간 초과
def f(num):
    summ = 0
    for i in range(1, num + 1):
        if num % i == 0:
            summ += i
    return summ

t = int(input())
for i in range(t):
    n = int(input())
    s = 0
    for j in range(1, n + 1):
        s += f(j)
    print(s)

#강의 풀이
#17427과 거의 동일한 문제. 다만, g(n)을 직접 구해놓는 작업 필요.
#g(n) = n의 약수의 합
#D[i] = g(i)

MAX = 1000000
#모든 약수에는 1이 들어가기 때문에 미리 넣어놓기.
d = [1] * (MAX + 1)
s = [0] * (MAX + 1)
#d를 먼저 모두 구하기. 각 수의 약수의 합 저장. 테스트 케이스에 따라 d는 달라지지 않는다.
for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        d[i * j] += i
        j += 1

#s[i] = d[1] + ... + d[i], 즉 g[i]
for i in range(1, MAX + 1):
    #s[i] = 1부터 i-1까지 + i
    s[i] = s[i-1] + d[i]

#받은 테스트케이스에 따라 입/출력하기.
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append(s[n])
print('\n'.join(map(str, ans)) + '\n')
