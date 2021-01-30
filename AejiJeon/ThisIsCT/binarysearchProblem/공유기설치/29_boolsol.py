
n, c = list(map(int, input().split()))
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
                                
start = array[1] - array[0]  # 무조건 처음, 마지막에 공유기를 설치 하는 경우에서 최대 거리가 나올 수밖에 없음 -> start 길이를 처음, 두 번째 elems 거리로 설정
end = array[-1] - array[0]  # 2개 설치 시 처음과 끝에 설치하게 되므로 at most 맨 끝 - 맨 처음
result = 0
print(start, end)
while(start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)