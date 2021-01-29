# 고정점 찾기
- 고정점: index=arr[index]인 원소
- 오름차순 정렬된 N개 원소 중, 고정점을 찾아 출력하세요!

## Solution
고정점보다 왼쪽의 값들은 `index > arr[index]`일 것이고  
오른쪽의 값들은 `index \< arr[index]`일 것이다.
그럼... 알지?