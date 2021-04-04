while True:
    n = input()
    if n == '0':
        break
    length = len(n)
    answer = 'yes'
    for i in range(length // 2):
        if n[i] != n[length - 1 - i]:
            answer = 'no'
            break
    print(answer)
'''    
    
#정답이 안되는 이유: 자릿수 한개에 대해 처리하지 못
while True:
    n = input()
    if n == '0':
        break
    length = len(n)
    answer = ''
    for i in range(length // 2):
        if n[i] == n[length - 1 - i]:
            answer = 'yes'
        else:
            answer = 'no'
    print(answer)
'''