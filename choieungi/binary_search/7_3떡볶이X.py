import sys

def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
            if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
                array[j], array[j - 1] = array[j - 1], array[j]
            else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break

def binary_search(array, target, start, end)

n, m= map(int, input().split())
rice_cake = list(map(int,sys.stdin.readline().split()))

rice_cake.sort()
h=rice_cake[n-1]

for i in range(n):
    for j in rice_cake.reverse():
        rice_cake.append(h)
        insert_sort(rice_cake)
        rice_cake[h]



