import sys
from collections import deque

input = sys.stdin.readline


for _ in range(int(input())):
    n, index = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    count = 0
    while True:
        # 맨 처음 들어온 문서 확인
        now = queue.popleft()
        # 마지막 남은 원소이거나 문서들 중 중요도가 제일 높은 경우
        if not queue or now >= max(queue):
            count += 1
            # 몇 번째로 인쇄되었는지 궁금한 문서가 pop된 경우
            if index == 0:
                break
        else:
            # 중요도가 제일 높지 않은 경우 다시 맨 뒤로 추가
            queue.append(now)
        # 위치가 한 칸 앞으로 땡겨지거나
        # 맨 앞에 있는 경우에는 맨 뒤로 추가
        index = index - 1 if index != 0 else len(queue) - 1

    print(count)
