# 상하좌우
import sys

n= int(input())                      #n 입력받기
x,y =1,1                             #처음 위치
plans = sys.stdin.readline().split() #문자열 한 문자씩 받기

dx = [0, 0, -1, 1] #x 방향 이동량
dy = [-1, 1, 0, 0] #y 방향 이동량
move_types = ['L','R','U','D'] # dx, dy를 인덱스에 맞춰 방향 지정

for plan in plans:
    for i in range(len(move_types)):
        if move_types[i]==plan:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<=0 or nx>5 or ny <=0 or ny>5:
        continue
    x, y = nx, ny

print(x,y)


