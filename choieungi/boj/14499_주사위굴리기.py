#boj_14499
n,m,x,y,k = map(int,input().split()) #map size, first_location, repeat
space = [ ]

dice = [[0]*3 for _ in range(4)]

#E:0 W:1 N:2 S:3
dx= [0,0,-1,1]
dy= [1,-1,0,0]

#space_information
for i in range(n):
    temp = list(map(int,input().split()))
    space.append(temp)

#move_information
command = list(map(int,input().split()))

def value(x,y):
    if space[x][y] ==0:
        space[x][y] = dice[1][1]
    else:
        dice[1][1] = space[x][y]
        space[x][y] = 0

    print(dice[3][1])
    #print(dice)

def move(cmd,x,y):
    global dice
    temp = [[0]*3 for _ in range(4)]
    if cmd ==0:
        temp[0][1],temp[2][1] = dice[0][1], dice[2][1]
        temp[1][0],temp[1][1],temp[1][2] = dice[1][1], dice[1][2],dice[3][1]
        temp[3][1] = dice[1][0]

    elif cmd ==1:
        temp[0][1],temp[2][1] = dice[0][1], dice[2][1]
        temp[1][0],temp[1][1],temp[1][2] = dice[3][1], dice[1][0],dice[1][1]
        temp[3][1] = dice[1][2]

    elif cmd == 2 :
        for i in range(3):
            temp[i][1]=dice[i+1][1]
        temp[3][1] =dice[0][1]
        temp[1][0],temp[1][2] = dice[1][0],dice[1][2]

    elif cmd==3:
        for i in range(3):
            temp[i+1][1]=dice[i][1]
        temp[0][1] =dice[3][1]
        temp[1][0],temp[1][2] = dice[1][0],dice[1][2]

    dice=temp
    value(x,y)

for i in command:
    direction_index = i-1
    nx = x + dx[direction_index]
    ny = y + dy[direction_index]
    if nx>=0 and nx<n and ny>=0 and ny<m:
        x,y = nx, ny
        #print(i)
        move(direction_index,x,y)


