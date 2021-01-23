# 부품 찾기

## Solution
N의 최대값이 100만, M의 최대값이 100만  
그냥 search하면, 최악의 경우 1,000,000,000,000번의 비교가 필요하게 됨  
  
따라서, binary search를 활용해서 문제를 풀어보자

## another solution
해쉬 맵을 사용해도 되겠다는 생각이 들었음.  
hash_map에 매장의 재고종류-개수 를 저장하면(c++에선 unordered_map),  
key가 있는지 없는지는 O(1)의 시간복잡도로 연산이 가능함

- c++ STL
    - map
        - Red-Black Tree사용: key의 순서 유지
        - insert, delete, search 모두 O(logn)
    - unordered_map은 
        - Hash Table사용: key순서 무시
        - 충돌 없는 경우, 평균 O(1) (그러나, 실제 시간은 더 느릴 수 있음)