#  0 0 0 0 0 0 
#  0 0 0 0 1 0
#  0 0 0 1 0 0
#  0 0 0 0 0 0
#  0 0 0 1 0 0
#  0 0 0 0 0 0

#  3초긑나고 아래방향
#  15초후 ㅚㄴ
#  17초후 아래
from collections import deque
n = int(input())

arr = [[0]*(n+1) for _ in range(n+1)] #(n+1)x(n+1)배열

k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    arr[x][y] = 1 #사과놓음

l = int(input())
queue_d = deque()
for _ in range(l):
    x, y = input().split()  # ('8', 'D')
    
    queue_d.append((int(x),y)) # [(8, 'D'), ...]

queue = deque()  # 뱀 담는 큐
queue.append((1,1)) # 꼬리, 머리
dir = 0 # 방향 초기화(오)

dx = [0,1, 0, -1]  # 동(0) 남(1) 서(2) 북(3)

dy = [1,0, -1, 0]

def turn(dir, c):
    if c == 'L':
        dir = (dir - 1)%4
    else:
        dir = (dir + 1)%4
    return dir

x, y = 1,1 # 시작  # 1초동안..
arr[x][y] = 2
time = 0
while True:   
    
    
    #이동전 계산 -> 몸닫거나벽
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and arr[nx][ny]!= 2: # 범위 안, 뱀에 안 들어감
        
        if arr[nx][ny] == 0: # 사과 없음
            arr[nx][ny] = 2
            queue.append((nx,ny))
            tx, ty = queue.popleft() # 꼬리 빼서 0처리
            arr[tx][ty] = 0
        
        if arr[nx][ny] == 1: #사과있음
            arr[nx][ny] = 2
            queue.append((nx,ny))

    else: # 다음 시간에 종료
        time += 1 
        break

    x,y = nx, ny
    time += 1

     

    if l > 0 and time == list(queue_d)[0][0]:
        
        c =queue_d.popleft()[1]
        
        dir = turn(dir, c)
        
        l -= 1
    
    

print(time)
    



