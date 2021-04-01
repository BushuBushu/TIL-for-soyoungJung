import math

def isPrime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False

n = int(input())
ns = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if isPrime(i):
        cnt += 1
        
print(cnt)