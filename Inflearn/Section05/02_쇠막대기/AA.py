import sys
sys.stdin = open('input.txt', 'r')

s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    #s에서 ')' 즉, 닫는 경우
    else:
        # 바로 앞이 '('인 경우, 즉 이것은 레이저이다. 즉, 갯수를 추가 해야함. len(stack)만큼! 또한 레이저는 지워버리기
        if s[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        # 바로 앞이 ')'인 경우, 즉 이것은 막대의 끝이다. cnt에 1을 더한다(마지막 자투리). 그리고 해당 막대의 첫부분인 stack의 끝을 pop해서 없앤다. 왜냐. 더이상 레이저에 잘릴 일이 없고 결국 cnt에 추가될 일이 없음.
        else:
            stack.pop()
            cnt += 1
    
print(cnt)
            
