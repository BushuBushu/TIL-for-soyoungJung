import sys
sys.stdin = open('input.txt', 'r')

a = input()
b = []
for x in a:
    b.append(x)

#연산을 수행할 것들.
stack = []

for i in range(len(b)):
    # i번째가 연산자라면. 더 좋은 방법이 있을 것 같기도..
    if b[i].isdigit() == False:
        #파이썬 슬라이스로 없애고 return하는 방법?
        stack.append(b.pop(i-2))
        stack.append(b.pop(i-1))
        stack.append(b.pop(i))
        
    print(stack)

#슬라이스로 빼내서 stack에 넣고, 그것의 return값을 b에다가 insert해서 새로운 b를 만들기..?
#반복문을 while문으로 바꿔야할 필요성은 있음. 

# 강의 풀이
# input을 하나씩 돌면서 연산자와 그 앞 두개를 두번 pop해서 꺼내서 결과를 다시 stack에 넣기!!

import sys
sys.stdin = open('input.txt', 'r')

a = input()
stack = []

for x in a:
    #숫자인 경우에는 stack에 그냥 쌓기
    if x.isdecimal():
        stack.append(int(x))
    #연산자인 경우 앞 두개를 pop해서 빼오기
    else:
        if x == '+':
            #stack에서 꺼낸 값을 변수에 저장하기. why? 연산의 순서를 맞춰줘야 하기 때문. 최근에 들어간 것이 뒤로 올 수 있도록
            bnum = stack.pop()
            fnum = stack.pop()
            stack.append(fnum + bnum)
        elif x == '-':
            bnum = stack.pop()
            fnum = stack.pop()
            stack.append(fnum - bnum)
        elif x == '*':
            bnum = stack.pop()
            fnum = stack.pop()
            stack.append(fnum * bnum)
        else:
            bnum = stack.pop()
            fnum = stack.pop()
            stack.append(fnum / bnum)

print(stack[0])
