import sys
sys.stdin = open('input.txt', 'rt')
num, m = map(int, input().split())
#str(num)을 하여 num을 하나하나 접근하여 숫자화하여 리스트에 넣는다.
num = list(map(int, str(num)))

stack = []
for x in num:
    #stack이 비어있으면 거짓, 즉 비어있지 않고, m이 셀 것이 남아 있으면, 또한 마지막 숫자가 나보다(x) 작은 경우에만!
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

# m개만큼 모두 지우지 못한 경우 맨 뒷자리를 m만큼 지워버림.
if m != 0:
    stack = stack[:-m]

#stack에 있는 것들이 스트링으로 모두 붙어 나온다
answer = ''.join(map(str, stack))
print(answer)