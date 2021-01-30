# 실수한 부분
O(logn)으로 특정 수 index 찾은 후 반복문을 통해 찾은 index로부터 양쪽으로 선형탐색을 함 -> 시간복잡도가 O(logn)을 넘어섬

# 효율적인 풀이
- 주어진 수의 첫 번째 위치 찾는 이진 탐색 함수와 마지막 위치를 찾는 이진 탐수 함수를 구현 -> 인덱스 차이를 계산하여 해결
- python의 binary search library인 **bisect**를 활용
'''python
from bisect import bisect_left, bisect_right
i = bisect_left(array, x) # x가 **처음**으로 나타나는 위치 반환
j = bisect_right(array, y) # y가 **마지막**으로 나타나는 위치 반환(index + 1)
#array에서 [left_value, right_value]인 데이터 개수 반환하는 함수(right_value는 포함하지 x, 값 여러개 있는 경우 제일 바깥쪽에 있는 위치로)
def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index
'''