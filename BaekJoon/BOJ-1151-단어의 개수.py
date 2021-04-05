'''
st = list(input())
cnt = 0

#앞 뒤 공백 제거
if st[0] == ' ':
    del st[0]
if st[-1] == ' ':
    del st[-1]

for i in st:
    if i == ' ':
        cnt += 1

print(cnt + 1)
'''
#split활용할 것. split을 저장해야 리스트가 된다.
st = input()
a = st.split()
print(len(a))