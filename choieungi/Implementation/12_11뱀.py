#북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n= int(input())
k= int(input())
game_map = [[0] * (n+1) for _ in range(n+1)]

#사과 위치 입력
for i in range(k):
    a,b = map(int,input().split())
    game_map[a][b]=1

def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

def turn_right(direction):
    direction+=1
    if direction == 4:
        direction = 0
    return direction

l = int(input()) #방향
directions =[]
for i in range(l):
    a,b= input().split()
    directions.append((int(a),b))


def game():
    x,y =1,1
    game_map[x][y]=2
    d = 1
    nail=[(x,y)] #뱀이 차지하는 공간의 위치
    index = 0 #회전 정보
    game_time =0 #게임 시간

    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if (nx>0 and nx<=n and ny>0 and ny<=n and game_map[nx][ny]!=2):
            if game_map[nx][ny]==1:
                game_map[nx][ny]=2
                nail.append((nx,ny))

            elif game_map[nx][ny]==0:
                game_map[nx][ny]=2
                nail.append((nx,ny))
                temp_x,temp_y = nail.pop(0) #큐
                game_map[temp_x][temp_y]=0
        else:
            game_time+=1
            break

        x,y = nx,ny
        game_time+=1

        if game_time==directions[index][0]:
            direction = directions[index][1]
            if direction == 'D':
                d= turn_right(d)
            else:
                d= turn_left(d)
            index+=1
    return game_time

print(game())











