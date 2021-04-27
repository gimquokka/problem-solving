n, m =map(int, input().split())
a,b,d = map(int, input().split())
game_space = []

#방향 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction=[0,1,2,3] #0:N 1:E 2:S 3:W
x,y, t= a, b, d

#게임 공간 만들기
for i in range(n):
    temp_list=list(map(int,input().split()))
    game_space.append(temp_list)

count =1

#인덱스 왼쪽으로 도는 것은 인덱스 -1하는 것임
while True:
    for _ in range(4):
        t = direction[direction.index(t) - 1]
        nx = x+dx[t]
        ny = y+dy[t]
        if game_space[nx][ny]==0 :
            game_space[nx][ny] = 2
            x,y=nx,ny
            count+=1
            continue
        else:
            nx,ny= x,y
            t = t

    if  game_space[x+dx[t-2]][y+dx[t-2]]==1:
        break
    else:
        game_space[x + dx[t - 2]][y + dy[t - 2]] = 2
        x,y = x + dx[t - 2], y + dy[t - 2]
        continue

print(count)






        #t = direction[direction.index(t) - 1]
        #if:






