# 배치 바꾸는 함수
# 하나의 리스트에 대해서(일정 구간의 리스트)

def change(l):
    for i in range(len(l) // 2):
        #기존 i값을 담는 임시 값
        tmp = l[i]
        l[i] = l[-i -1]
        l[-i -1] = tmp
    return l

cards = list(range(1, 21))


for i in range(10):
    ai, bi = map(int, input().split())
    li = cards[ai - 1 : bi]
    cards[ai - 1 : bi] = change(li)

for i in cards:
    print(i, end = ' ')

# 강의 풀이
'''
a = list(range(21))
# 변수 없이 반복하기
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]

# 앞에 0버리기
a.pop(0) #0번인덱스에 있는 것을 pop하라는 것.
for x in a:
    print(x, end = ' ')
'''