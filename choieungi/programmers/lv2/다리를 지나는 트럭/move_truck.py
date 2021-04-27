from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    # queue_bridge = deque(bridge)
    queue_truck_weights = deque(truck_weights)

    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if queue_truck_weights:
            if sum(bridge) + queue_truck_weights[0] <= weight:
                bridge.append(queue_truck_weights.popleft())
            else:
                bridge.append(0)

    return time
