
import sys


wheels = [0]

# append lists of 1,2,3,4 wheels
for i in range(1, 5):
    wheels.append(list(map(int,list(input())))) 

# move all elements of array to right 
# last elem to first 
def move_cw(arr):
    n = len(arr)
    temp = [0]*n
    for i in range(n-1):
        temp[i+1] = arr[i]
    temp[0] = arr[n-1]

    return temp

# move all elements of array to left
# first elem to end 
def move_ccw(arr):
    n = len(arr)
    temp = [0]*n
    for i in range(n-1, 0, -1):
        temp[i-1] = arr[i]
    temp[n-1] = arr[0]

    return temp

k = int(input())

for i in range(k):
    num, d = map(int, input().split())

    # 회전하는 톱니 바퀴의 9시, 3시 방향의 극
    l, r = wheels[num][6], wheels[num][2]

    # 회전
    wheels[num] = move_cw(wheels[num]) if d == 1 else move_ccw(wheels[num])

    
    nd = d
    # 왼쪽에 있는 톱니 바퀴들 순서대로 확인
    for num_l in range(num-1, 0, -1):
        # 9시, 3시 방향의 극
        ll, rr = wheels[num_l][6], wheels[num_l][2]

        # 회전하는 오른쪽에 있는 톱니 바퀴의 9시 방향의 극과
        # 해당 톱니 바퀴의 3시 방향의 극이
        # 같은 경우 -> 회전하지 않고 멈춤 
        # -> 나머지 왼쪽에 있는 톱니 바퀴들은 고려하지 않음
        if l == rr:
            break
        # 방향의 극이 다른 경우
        # 오른쪽 톱니가 회전하는 방향 반대로 
        # 해당 톱니 바퀴가 회전
        else:
            
            if nd == 1:
                wheels[num_l] = move_ccw(wheels[num_l])
                nd = -1
            else:
                wheels[num_l] = move_cw(wheels[num_l])
                nd = 1
            # 다음 왼쪽 톱니바퀴의 3시 방향의 극과 
            # 회전하는 톱니 바퀴의 9시 방향의 극을
            # 확인하기 위해 새로 할당
            l = ll

    # 오른쪽
    nd = d
    for num_l in range(num+1, 5):
        ll, rr = wheels[num_l][6], wheels[num_l][2]

        if r == ll:
            break
        else:
            if nd == 1:
                wheels[num_l] = move_ccw(wheels[num_l])
                nd = -1
            else:
                wheels[num_l] = move_cw(wheels[num_l])
                nd = 1
            r = rr

sum = 0

for i in range(1, 5):
    if wheels[i][0] == 1:
        sum += 2 ** (i-1)
    

print(sum)