m = list(map(int, input().split()))
'''
flag = ''
for i in range(0, 7):
    if m[i] + 1 == m[i + 1]:
        flag = 'ascending'
    elif m[i] - 1 == m[i + 1]:
        flag = 'descending'
    else:
        flag = 'mixed'

print(flag)
'''
#참고 풀이

if m == sorted(m):
    print('ascending')
elif m == sorted(m, reverse = True):
    print('descending')
else:
    print('mixed')

