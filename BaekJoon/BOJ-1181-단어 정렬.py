'''n = int(input())

words = [input() for _ in range(n)]

#중복없애기
nowords = list(set(words))

#len으로 sort하기
lenw = sorted(nowords, key = lambda x : len(x))

print(lenw)


#해당 방법은 같은 길이의 단어가 여러개일 경우 적용되지 않는다.
for i in range(len(lenw) - 1):
    if len(lenw[i]) == len(lenw[i + 1]):
        if lenw[i] > lenw[i + 1]:
            #print(lenw)
            print(lenw[i], lenw[i + 1])
            lenw[i], lenw[i + 1] = lenw[i + 1], lenw[i]
            
print(lenw)'''

n = int(input())
words = []

for _ in range(n):
    word = input()
    word_cnt = len(word)
    words.append((word, word_cnt))

#중복제거
words = list(set(words))

#단어의 갯수(x[1])와 단어의 크기(알파벳순,x[0]) 조건을 중복 적용

words.sort(key = lambda x: (x[1], x[0]))

for w in words:
    print(w[0])