# 이진 탐색
배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘.  
탐색 범위를 절반씩 좁혀가며 데이터를 탐색한다.  
  
탐색과정에서 '시작점' '끝점' '중간점' 세 변수를 사용하는데,  
**찾으려는 데이터**와 **중간점**위치의 데이터를 반복적으로 비교하는것이 주 과정이다.  
0. 오름차순 정렬
1. 중간점 = (시작점 + 끝점)/2
2. 중간점과 찾으려는 데이터 비교
    if 중간점 < 찾으려는 데이터, 시작점 = 중간점+1  
    if 중간점 > 찾으려는 데이터, 끝점 = 중간점-1
3. 중간점 == 찾으려는 데이터 일 때 까지 `1`,`2` 반복
- 시간복잡도
    - O(logn)
- 구현
1. 재귀함수
    ~~~cpp
    //Recursive
    //해당 index 반환 or -1반환
    int binary_search(int start, int end) {
        if (start > end) { //start랑 end가 엇갈리면 없는거임
            return -1;
        }
        int mid = (start+end)/2;
        if (arr[mid] < target) {
            return binary_search(mid+1, end);
        }
        if (arr[mid] > target) {
            return binary_search(start, mid-1);
        }
        return mid;
    }
    ~~~
2. 반복문
    ~~~cpp
    //Iterative
    //index반환
    int binary_search () {
        while (start <= end) {
            mid = (start + end) / 2;
            if (arr[mid] == target) {
                return mid;
            }
            if (arr[mid] < target) {
                start = mid + 1;
            }
            if (arr[mid] > target) {
                end = mid - 1;
            }
        }
        return -1;
    }
    ~~~


# 트리 자료구조
데이터베이스 시스템, 파일 시스템 등에서 대용량 데이터를 보관할때 주로 사용되는 구조  
- 특징
    - 트리는 부모노드와 자식노드의 관계로 표현된다
    - 최상단 노드를 루트 노드라고 한다
    - 최하단 노드를 단말 노드라고 한다
    - 트리에서 일부를 떼어내도 트리이며, 이를 서브 트리라고 한다
    - 트리는 파일 시스템과 같이 **계층적이고 정렬된 데이터**를 다루기 적합하다
## 이진 탐색 트리
이진 탐색이 동작할 수 있도록 고안된 트리 자료 구조.  
- 특징
    - 부모노드보다 왼쪽 자식노드가 작다
    - 부모노드보다 오른쪽 자식 노드가 크다
- 이진 탐색 트리에서 데이터를 조회하는 과정
    1. 루트노드와 target을 비교
        - 루트노드 < target 이면, 오른쪽 자식 노드 방문
        - 루트노드 > target 이면, 왼쪽 자식 노드 방문
        - 루트노드 == target이면, 탐색을 마침
    2. 방문한 노드를 루트 노드로 하는 서브트리에서 `1`반복