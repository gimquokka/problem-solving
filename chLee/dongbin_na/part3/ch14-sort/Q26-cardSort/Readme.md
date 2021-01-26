# 카드 정렬

## Solution
맨 앞에 두개 더하고, `insert`...  
-> O(N^2)이 걸림 ㅠ

## Solution - official
`Heap`을 이용하면 제일 작은 두 원소를 뽑는데 시간이 O(logN)이 소요된다  
-> 총 시간 복잡도 O(NlogN)