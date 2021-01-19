# sort

## 선택 정렬 
정렬이 안 된 숫자 중, 가장 작은 숫자를 선택해 앞으로 보내는 방식
- source code
    ~~~cpp
    // 오름차순
    for (int i=0; i<arr.size(); i++) {
        int min_index = i; //0부터 i-1까지는 다 정렬이 되어 있는 상태
                            //최소값은 index 'i'부터 찾아가면 된다
        for (int j=i+1; j<arr.size(); j++) {
            if (arr[min_index] > arr[j]) {
                min_index = j;
            }
            swap(arr[min_index], arr[j]);
        }
    }
    ~~~
- 시간 복잡도
    O(n*n)

## 삽입 정렬
정렬이 안 된 숫자중 하나를, 정렬이 된 숫자에 삽입하는 방식
- source code
    ~~~cpp
        // 오름차순
    for (int i=0; i<arr.size(); i++) {
            for (int j=i; j>0; j--) {
                if (arr[j] < arr[j-1]) {
                    swap(arr[j], arr[j-1]);
                }else{
                    break;
                }
            }
        }
    ~~~
- 시간 복잡도
    O(n*n)  
    대신, 기존 정렬 상태에 따라서 선택 정렬보다 빠르게 동작한다  

## 퀵 정렬
기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다
- source code
    ~~~cpp
    void quick_sort (int start, int end) {
        if (start >= end) { //원소가 한 개 인 경우
            return;
        }
        int pivot = start; //피벗을 첫 번째 원소로 함
        left = start + 1;
        right = end;
        
        while (left <= right) {
            //피벗보다 큰 값 찾기
            while (left <= end && arr[left] <= arr[pivot]) {
                left += 1;
            }
            //피벗보다 작은 값 찾기
            while (right > start && arr[right] >= arr[pivot]) {
                right -= 1;
            }
            if (left > right) { //엇갈렸으면, 피벗과 작은 값 swap
                swap(arr[right], arr[pivot]); 
            } else {
                swap(arr[right], arr[left]); 
            }
        }
        // 피벗에 대해 분류를 끝낸 다음, 재귀함수로 왼쪽, 오른쪽 분류 시작
        // 마지막에 right자리에 있던게 pivot임 ㅇㅇ
        quick_sort(start, right-1);
        quick_sort(right+1, end);
    }
    ~~~
- 시간 복잡도
    O(nlogn)

## 계수 정렬
(특정 조건에 부합할 대만 사용할 수 있지만, 조건만 맞으면 굉장히 빠른 알고리즘)  
최소부터 최대까지 그 사이의 모든 수가 등장한 개수를 세고, 순차적으로 출력하면 됨
- 조건
    모든 데이터가 양의 정수, 데이터의 최대값과 최소값의 크기 차이가 많이 나지 않을때
- 시간 복잡도
    O(n + k) //k는 데이터의 최대 값
- source code
