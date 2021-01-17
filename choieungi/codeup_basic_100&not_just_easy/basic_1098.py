import sys
num=[ ]
a,b=map(int,input('').split())
for i in range(a):
    line=[]
    for j in range(b):
        line.append(0)
    num.append(line)

#막대 개수 받기
c,d=0,0
k=int(input())
for i in range(k):
    list=sys.stdin.readline().split() #막대 정보 받는 리스(길이, 방향, 좌표)
    for j in range(int(list[0])): #길이 만큼
        c= int(list[2])
        d= int(list[3]) # 좌표 설정
        if list[1] =='0': #방향 설정
            if num[c-1][d+j-1] == 0:
                num[c-1][d+j-1] = 1

        elif list[1]=='1':
            if num[c+j-1][d-1] == 0:
                num[c+j-1][d-1] = 1


#결과 출력
for i in range(a):
    for j in range(b):
        print(num[i][j],end=' ')
    print('')

