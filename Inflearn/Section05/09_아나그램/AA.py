import sys
#sys.stdin = open('input.txt', 'r')

fw = input()
sw = input()
alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
fdic = {}
sdic = {}

for x in alph:
    fdic[x] = 0
    sdic[x] = 0
    
for x in fw:
    fdic[x] += 1

for x in sw:
    sdic[x] += 1
    
if fdic == sdic:
    print('YES')
else:
    print('NO')

#강의 풀이
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print('No')
            break   
    else:
        print('NO')
        break
    
else:
    print('YES')

#개선된 강의 풀이
# 두번째 입력 문자를 돌 때 -1을 시킴으로써, 모든 key값이 0일 때 참이 된다.

a = input()
b = input()
sh = dict()
for x in a:
    sh[x] = sh.get(x, 0) + 1
for x in b:
    sh[x] = sh.get(x, 0) - 1

for x in a:
    if sh.get(x) > 0:
        print('No')
        break
else:
    print('yes') 