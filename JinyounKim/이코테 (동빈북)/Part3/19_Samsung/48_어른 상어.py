"""
문제풀이 전략
Key! 어떻게 구현의 복잡도를 낮출 것인가?
    (1) 일단 복잡해 보인다고 쫄지 말기
    (2) 냄새는 smell로 상어의 현재 위치는 arr로 나누어서 저장하기
    (3) 어떤 부분을 함수로 나눌지 생각 => update_smell, move로 나누기
    (4) 종이에 명세서를 한번 적어보기
    (5) 문제 정확히 여러번 읽고 제약조건과 구현해야하는 부분 적확히 확인하기

"""
# 입력 받기
n, m, k = map(int, input().split())

# N x N 입력
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 방향 입력 받기
directions = list(map(int, input().split()))

# 우선순위 입력 받기
priorities = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        priorities[i].append(tuple(map(int, input().split())))

# smell 정보를 담을 arr선언
smell = [[[0, 0]]*n for _ in range(n)]

# print(smell)
# smell arr를 arr에 맞춰 update
def update_smell():
    global smell
    for x in range(n):
        for y in range(n):
            # 만약 시간이 남앗다면
            if smell[x][y][1] > 0:
                smell[x][y][1] -= 1
            # 상어의 이동위치 반영하기
            if arr[x][y] != 0:
                smell[x][y] = [arr[x][y], k]


# dx, dy 선언
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어를 이동시켜줄 move 함수 선언
def move():
    global arr
    new_arr = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 상어가 있다면
            if arr[x][y] != 0:
                num = arr[x][y]
                direction = directions[num-1]
                found = False
                # 우선순위에 따라 주변 4방향 탐색
                # priorities 상어번호-1 => 현재이동번호-1 => 우선이동순위번호-1
                for i in range(4):
                    nx = x + dx[priorities[num-1][direction-1][i]-1]
                    ny = y + dy[priorities[num-1][direction-1][i]-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 냄새가 없는 칸이라면
                        if smell[nx][ny][1] == 0:
                            # 상어의 방향 바꿔주기
                            directions[num-1] = priorities[num -
                                                           1][direction-1][i]
                            # 이동할 방향이 빈칸이라면
                            if new_arr[nx][ny] == 0:
                                new_arr[nx][ny] = num
                            # 이동할 방향에 상어가 있다면
                            else:
                                new_arr[nx][ny] = min(new_arr[nx][ny], num)
                            found = True
                            break
                if found:
                    continue
                # 자신의 냄새가 있는 경우는 빈칸 다 조사하고 임으로
                for i in range(4):
                    nx = x + dx[priorities[num-1][direction-1][i]-1]
                    ny = y + dy[priorities[num-1][direction-1][i]-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 자신의 냄새가 있는 경우
                        if smell[nx][ny][0] == num:
                            # 상어의 방향 바꿔주기
                            directions[num-1] = priorities[num -
                                                           1][direction-1][i]
                            # 이동할 방향은 무조건 빈칸임 왜냐하면 다른 상어들은 이 칸에 못들어 옴으로
                            new_arr[nx][ny] = num
                            break
    return new_arr


time = 0
for _ in range(1000):
    time += 1
    update_smell()
    arr = move()

    check = True
    for x in range(n):
        for y in range(n):
            # 만약 1보다 큰 상어가 있다면
            if arr[x][y] > 1:
                check = False
    # 1만 있다면
    if check == True:
        print(time)
        quit()
# 1000초를 넘겼다면
print(-1)
