import sys
#sys.stdin = open("input.txt", 'r')

cube = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
def chk(l):
    for i in range(len(l) // 2):
        if l[i] != l[len(l) - 1 - i]:
            return False
    return True

#행체크
for i in range(7):
    for j in range(3):
        #print(cube[i][j:j+5])
        if chk(cube[i][j:j+5]):
            cnt += 1
            #print('ad')
    #print('--')

#열체크, 열을 행의 형태로 재배열하여 검증. 더 좋은 방법이 있을듯!!
colcube = []
for i in range(7):
    col = []
    for j in range(7):
        col.append(cube[j][i])
    colcube.append(col)

for i in range(7):
    for j in range(3):
        #print(colcube[i][j:j+5])
        if chk(colcube[i][j:j+5]):
            cnt += 1
            #print('ad')
    #print('--')

print(cnt)
        
# 강의 풀이
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i : i + 5]
        if tmp == tmp[::-1]:
            cnt += 1 #여기까지는 나와 비슷
# 열의 경우는 슬라이스를 사용할 수 없음. 따라서 다음과 같이

        for k in range(2):#길이의 몫만큼만, 5를 2로 나눈 몫만큼(나의 chk 함수와 동일한 원리)
            #j는 계속 동일하게. 하나의 열에 대하여 비교해야하기 때문에
            if borad[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1