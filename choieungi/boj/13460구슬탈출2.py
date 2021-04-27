'''
1. 처음에 구슬의 위치를 .으로 변경하고 구슬의 위치를 큐에 넣는다.
2. 구슬을 벽이나 구멍에 갈때 까지 움직인다.(반복문 종료)
3-1. 파란 구슬이 구멍에 들어가는 경우에 반복문을 다시 진행해 다른 방향으로 기울인다(움직인다)
3-2. 파란 구슬과 빨간 구슬이 같은 위치에 있다면 거리가 더 가까운(이동거리가 더 짧은)것을 그대로 두고 먼 것을 바로 이전의 위치에 둔다.
3-3. 이동한 위치가 갔던 곳이면 큐에 넣고 아니면 진행
4. 가능한 방향(max 4)을 모두 탐색하고 cnt 1 증가, 어딜 갔든 간에 1번 간 것은 자명하므로.

'''


from collections import deque
n, m = map(int, input().split())

space =[0] * n
for i in range(n):
    space[i] = list(map(str, input()))

for i in range(n):
    for j in range(m):
        if space[i][j] == "R":
            rx,ry = i,j
            space[i][j] = '.'
        if space[i][j] == "B":
            bx,by=i,j
            space[i][j] = '.'

#print(space)
dx=[0,0,-1,1]
dy=[-1,1,0,0]
cnt = 0
queue = deque()
check_queue = deque()
def bfs(rx,ry,bx,by,space,cnt):

    queue.append((rx,ry,bx,by))
    while queue:
        qlen = len(queue)
        while qlen:
            rx, ry, bx, by = queue.popleft()
            if space[rx][ry] == 'O':
                print(cnt)
                return
            for i in range(4):
                nrx,nry,nbx,nby = rx,ry,bx,by
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if space[nrx][nry] == "O":
                        break
                    if space[nrx][nry] == "#":
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if space[nbx][nby] == "O":
                        break
                    if space[nbx][nby] == "#":
                        nbx -= dx[i]
                        nby -= dy[i]
                        break

                if space[nbx][nby] == "O":
                    continue

                if nbx == nrx and nby == nry:
                    if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx,nry,nbx,nby) not in check_queue:
                    check_queue.append((nrx,nry,nbx,nby))
                    queue.append((nrx,nry,nbx,nby))
            qlen -=1
        if cnt == 10:
            print(-1)
            return
        cnt+=1
    print(-1)
    return

bfs(rx,ry,bx,by,space,cnt)