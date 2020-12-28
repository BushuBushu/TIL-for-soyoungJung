# 내 풀이

import math
#x는 스트링으로 받기
def reverse(x):
    rev = ''
    for a in range(len(x), 0, -1):
        rev += x[a - 1]
    return int(rev)

def isPrime(x):
    if x == 1:
        return False
    y = 0
    for i in range(1, x + 1):
        if x % i == 0:
            y += 1
    if y >= 3:
        return False
    else:
        return True

N = int(input())
l = list(input().split())

#숫자를 모두 뒤집은 리스트
revl = []
for n in l:
    revl.append(reverse(n))


# 거꾸로 된 숫자 중 소수 찾기
for num in revl:
    if isPrime(num):
        print(num, end = ' ')
    
# 강의 풀이
'''
def reverse(x):
    res = 0
    while x > 0:
        t = t % 10
        x = x // 10
        res = res * 10 + t
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
        else:
            return True
            
n = int(input())
a = list(map(int, input().split()))
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end =" ")
'''