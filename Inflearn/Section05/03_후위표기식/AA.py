#내 풀이
import sys
#sys.stdin = open('input.txt.', 'r')

ex = input()
num = '123456789'
nstack = []
estack = []

for i in ex:
    if i in num:
        nstack.append(i)
    else:
        estack.append(i)
print(estack)            
        
#print(nstack, estack)

for _ in range(len(estack)):
    nstack.append(estack.pop())

print(nstack)

# 강의 풀이
# 중요한 것은 연산자를 담는 논리. 

import sys
sys.stdin = open('input.txt', 'r')
a = input()
#연산자를 담을 stack
stack = []
#정답
res = ''

for x in a:
    #피연산자인 경우, 답에 append하기.
    if x.isdecimal():
        res += x
    #연산자인 경우 처리
    else:
        # 연산자 중 괄호를 만난 경우
        if x == '(':
            #무조건 append하기. 이것이 우선순위가 가장 높기 때문.
            stack.append(x)
        # 연산자가 곱하기/나눗셈인 경우
        elif x == '*' or x == '/':
            #stack이 빌 때까지 & stack의 top이 곱하기이거나 나누기가 아닐 때까지 stack에서 pop한 뒤 res에 붙이기
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            # 더하기 빼기의 경우 자기보다 stack에 있는 것이 빠름. 같은 더하기/빼기더라도, 자신보다 왼쪽에 있는 것이기 때문에 빠름. 따라서 모두 끄집어 내기.
            # 언제까지 끄집어 내는가? stack이 빌 때까지. & stack의 top이 (가 아닐 때까지. 여는 괄호 전까지만 끄집어 내기.
            # 여는 괄호가 있다는 것은, 괄호 안의 더하기 빼기라는 의미.
            #stack에 무언가 있을 때까지(stack이 없으면 걍 append함). & stack의 top이 (가 아닐 때까지. 즉, (인 경우에는 while문이 돌지 않음. 즉, 중괄호 안에 있는 것은 먼저 처리하고 해당 x를 append하겠다는 것.
            #stack[-1] != '(' 이해가 잘 안됨.
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        # 여는 괄호까지 모든 걸 처리한다. 위와 동일함. 괄호 안의 연산자를 모두 pop해줘야 함.
        elif x == ')':
            while stack and stack[-1] != '(':
                # 여는 괄호 만나면, 그 괄호 안의 있는 것 처리
                res += stack.pop()
            # 여는 괄호는 없애버리기
            stack.pop

#연산자가 stack에 남아있는 경우 모두 pop으로 처리해주기.
while stack:
    res += stack.pop()
print(res)

