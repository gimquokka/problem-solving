from collections import deque
import time

start = time.time()

'''
bridge = [0] * 10000000
for _ in range(100):
    print(sum(bridge), end=' ')
#time:7.6753082275390625

bridge = [0] * 10000000
queue = deque(bridge)
for _ in range(100):
    print(sum(queue), end=' ')
#time 8.506721496582031
'''

print('')
print(time.time()-start)



