import sys
sen_list =[ ]
sen_num = int(input(""))

for i in range(sen_num):
    sensor = int(sys.stdin.readline())
    sen_list.append(sensor)

#2번 딕셔너리를 이용해 계산 (이 부분 중요, 생각하기 어려웠음)
count= {}
for i in sen_list:
    try: count[i] += 1
    except: count[i] = 1

#3번 정렬 이용
count_list = list(count.values())

my_set = set(count_list) #집합set으로 변환
count_list = list(my_set) #list로 변환
count_list.sort(reverse=True) #빈도수를 내림차순 정렬

#3-1 빈도 수 중복 값 확인
max_sensors = []  # 최대인 것들을 모으는 리스트
sec_sensors = []  # 두번인 것들을 모으는 리스트

for key, value in count.items(): #count에 아이템을 하나씩 접근해서, key, value를 각각 name, age에 저장
    if value == count_list[0]:
        max_sensors.append(key)
    elif value == count_list[1]:
        sec_sensors.append(key)

if len(max_sensors)>1:
    print(max(max_sensors)-min(max_sensors))
else:
    abs_value= []
    for i in sec_sensors:
        abs_value.append(abs(max_sensors[0]-i))
    print(max(abs_value))



