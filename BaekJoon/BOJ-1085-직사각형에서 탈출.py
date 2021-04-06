import math
x, y, w, h = map(int, input().split())

a = w - x
b = h - y

#x, y를 비교하는 이유: 직사각형의 경계는 (0, 0)부터 시작이다.
print(min(a, b, x, y))