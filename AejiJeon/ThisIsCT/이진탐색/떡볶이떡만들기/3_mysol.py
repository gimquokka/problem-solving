import sys
n, m = map(int, input().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort(reverse = True)

start = 0
end = n-1


def lengh_left(array, cut_l):# 남은 길이 계산
    leng = 0
    for elem in array:
        l = elem - cut_l
        if l > 0:
            leng += l

    return leng


while True:
    if start > end:   # mid와 end 사이의 숫자에서 나타남
        
        _m = min(start, mid, end)        # min값부터 1씩 증가시켜서 도출
        
        check_fl = (m - leftleng) / (_m + 1)  # leftleng + (_m + 1)* x = m 이 되는 해 x를 찾음    

        minus_count = int(check_fl) if check_fl == int(check_fl) else int(check_fl)+1 
       
        result = arr[_m] + minus_count  
        break

    mid = (start + end) // 2

    leftleng = lengh_left(arr[:mid+1], arr[mid]) 
    
    if leftleng == m:
        result = arr[mid]
        break

    elif leftleng > m:
        end = mid - 1
    
    else:
        start = mid + 1


print(result)
