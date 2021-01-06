import sys
sys.stdin = open("input.txt", 'r')
su = [list(map(int, input().split())) for _ in range(9)]

check = True
# 각 행에 중복이 없는지 확인, 리스트를 인자로 받기
def rowcol(l):
    for i in l:
        if l.count(i) >= 2:
            return False
    return True

#인자로 열로 이루어진 리스트 받기. 열로 이루진 리스트 만들

# 행 / 열 확인
for i in range(9):
    row = []
    col = []
    for j in range(9):
        row.append(su[i][j])
        col.append(su[j][i])
    #print("row",row)
    #print("col",col)
    if rowcol(row) and rowcol(col):
        check = True
    else:
        check = False
        break

#3행3열 확인 - 실패함!!!

#강의 풀이
import sys
sys.stdin = open("input.txt", "r")
def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            #행의 값
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    #그룹 검사
    for i in range(3):
        for j in range(3):#여기까지가 상단 1개그룹 검사
            ch = [0] * 10
            for k in range(3):
                for s in range(3):
                    #해당 인덱스 이해하기!!!
                     #k는 행, s는 열을 증가시킴. 주어진 격자판의 인덱스의 값을 읽기 위한 것이 아님!!
                    #print(i, j, k, s)
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            #이 자리에 왜 if가 있는지도 생각해보기
            if sum(ch3) != 9:
                return False
    return True


            


            
    
    

        
