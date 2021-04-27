#27 찾는 원소의 개수를 출력하는 알고리즘
n, m = map(int,input().split())
element = list(map(int, input().split()))

def binary_search (array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif target <= array[mid]:
            end = mid -1
        else:
            start = mid +1
    return -1

answer = 0
temp = n-1
while binary_search(element,m,0,temp)!=-1:
    if binary_search(element,m,0,temp) != -1 :
            answer += 1
            element.pop(binary_search(element,m,0,n-1))
            temp -=1

if binary_search(element, m, 0, temp) == -1:
    print('-1')
else:
    print(answer)


