from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(4)
queue.append(5)
queue.append(6)
queue.popleft()

print(queue)
queue.reverse()
print(queue)