#boj_14891
import copy

#톱니바퀴 정보를 받는 리스트
wheels = []

for i in range(4):
    temp1 = input() # N:0 S:1
    temp2 = []
    for j in range(8):
        temp2.append(int(temp1[j]))
    wheels.append(temp2)

def clockwise(arr):
    new_arr = copy.deepcopy(arr)
    for i in range(8):
        try:
            new_arr[i+1] = arr[i]
        except:
            new_arr[0] = arr[7]
    return new_arr


def counterclockwise(arr):
    new_arr = copy.deepcopy(arr)
    for i in range(8):
        try:
            new_arr[i] = arr[i+1]
        except:
            new_arr[7] = arr[0]
    return new_arr

k= int(input()) #rotation_num

after_wheels = copy.deepcopy(wheels)

for i in range(k):
    wheel, direction = map(int,input().split())  # 1: clock -1:counterclock
    wheel_index = wheel-1

    a,b= wheel_index, wheel_index # 0<= a,b <4

    temp_direction = direction
    while(a!=0): #go to left
        if wheels[a-1][2] != wheels[a][-2]: #왼쪽에 있는 톱니의 2번째 인덱스. 오른쪽 톱니의 -2번째 인덱스를 비교
            if temp_direction==1:
                after_wheels[a-1] = counterclockwise(wheels[a-1])
            else:
                after_wheels[a-1] = clockwise(wheels[a-1])
            temp_direction= -(temp_direction) #이웃 바퀴는 반대 방향으로
            a -=1

        else:
            break

    temp_direction = direction # temp 방향 초기화
    while (b != 3):  # go to right
        if wheels[b][2] != wheels[b+1][-2]:
            if temp_direction == 1:
                after_wheels[b + 1] = counterclockwise(wheels[b+1])
            else:
                after_wheels[b+1] = clockwise(wheels[b + 1])
            temp_direction = -(temp_direction)
            b += 1

        else:
            break

    #기준이 되는 톱니 회전
    if direction ==1:
        after_wheels[wheel_index] = clockwise(wheels[wheel_index])
    else:
        after_wheels[wheel_index] = counterclockwise(wheels[wheel_index])

    #copy.deepcopy 반드시 왜냐하면 after_wheels가 수정될 때 wheel도 바뀌어서 반복문을 여러번 돌리면 원하는 값으로 할당이 안됨. 이것 때문에 백준에서 틀림
    wheels = copy.deepcopy(after_wheels)

score = 0
temp_score = 1 #1,2,3,4로 갈수록 2배로 점수(1,2,4,8)가 올라 그에 상응하는 매개변수 선언

for wheel_score in wheels:
    if wheel_score[0] == 1: # S극이면
        score += (temp_score * 1)

    temp_score *= 2

print(score)
