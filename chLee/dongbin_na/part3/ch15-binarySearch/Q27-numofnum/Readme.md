# 정렬된 배열에서 특정 수의 개수 구하기

## Solution
이분탐색 알고리즘을 조금 변경해서, x를 가지는 index를 찾았을 때  
양 옆으로 선형탐색을 시행함  

## Solution - official
- `algorithm`헤더에 존재하는 `upper_bound( )`와 `lower_bound( )` 함수를 사용해서, 해당 원소가 존재하는 가장 큰 index와 가장 작은 index를 구해서 빼줌
