def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    # 아래로 이동, 오른 쪽으로 이동, 왼쪽 위로 이동(변화량)
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    x, y, d = 0, 0, 0
    num = 1

    while True:
        answer[x][y] = num
        nx = x + dx[d]
        ny = y + dy[d]
        # index 범위를 벗어나거나 다음으로 이동할 칸에 이미 숫자가 적힌 경우
        if (nx >= n or ny >= n) or answer[nx][ny] != 0:
            # 방향 전환
            d = (d + 1) % 3
            nx = x + dx[d]
            ny = y + dy[d]
            # 방향 전환 했는데도 숫자를 적을 수 없는 경우
            # 즉, 숫자들이 다 채워진 경우
            if (nx >= n or ny >= n) or answer[nx][ny] != 0:
                break
        x, y = nx, ny
        num += 1

    return [answer[i][j] for i in range(n) for j in range(i + 1)]


print(solution(1))
