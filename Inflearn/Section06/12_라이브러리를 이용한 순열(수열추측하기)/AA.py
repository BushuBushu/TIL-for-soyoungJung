import sys
import itertools as it
sys.stdin = open('input.txt', 'r')
n, f = map(int, input().split())
b = [1] * n
cnt = 0

#곱할 이항 계수 배열 만들기
for i in range(1, n):
    b[i] = b[i-1] * (n-1) / i

a = list(range(1, n + 1))
#a의 permutations구하기
for tmp in it.permutations(a):
    sum = 0
    #각 permutation에 접근하기.
    #enumerate로 하는 이유. 인덱스 L을 사용하여 같은 위치 인덱스(순열 인덱스와 b배열-이항계수)에 있는 값끼리 곱해줘야 한다.
    #x는 순열 안에 하나하나 값.
    for L, x in enumerate(tmp):
        sum += (x * b[L])
    if sum == f:
        for x in tmp:
            print(x, end = ' ')
        break
