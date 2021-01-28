#내 풀이. 해시를 사용하지 x
import sys
#sys.stdin = open('input.txt', 'r')
n = int(input())
words = []
poem = []

for _ in range(n):
    words.append(input())
    
for _ in range(n-1):
    poem.append(input())
    
for x in words:
    if x not in poem:
        print(x)

#강의를 듣고 나서.. 딱히 dict의 장점을 모르겠음.
import sys
#sys.stdin = open('input.txt', 'r')
n = int(input())
dic = dict()

for _ in range(n):
    dic[input()] = 0

for _ in range(n-1):
    x = input()
    dic[x] = 1

for k, v in dic.items():
    if v != 1:
        print(k)
