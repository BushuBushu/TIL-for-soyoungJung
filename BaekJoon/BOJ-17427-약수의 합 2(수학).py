#내 풀이 - 시간초과
#한 수의 약수의 합
def f(num):
    summ = 0
    for i in range(1, num + 1):
        if num % i == 0:
            summ += i
    return summ
            
n = int(input())
nl = list(range(1, n + 1))
s = 0
for i in nl:
    s += f(i)
    
print(s)

#강의 풀이
#약수의 반대 == 배수 를 활용하여 풀기, 실제로 약수 구할 경우 시간복잡도 높음.
#A를 약수로 갖는 수 == A의 배수

n = int(input())
res = 0

#i는 약수.
for i in range(1, n + 1):
    #n // i는 i의 배수의 개수. 즉, i를 약수로 갖는 수.
    #n//i에 i를 곱하면 i라는 수가 몇 번 더해지는지 구할 수 있음.
    #i마다 모두 더하면 g(n)을 구하는 것.
    res += (n // i) * i
print(res)
