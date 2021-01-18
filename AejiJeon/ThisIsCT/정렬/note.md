# 개념 짚고 넘어가기  
- 내림차순 정렬 -> 오름차순 정렬 알고리즘에서 크기 비교 반대로 수행4
- selection, insertion sort 둘다 O(N^2)이지만 insertion의 경우에 list가 이미 정돈되었을 경우 O(N) 
- quick sort는 avg O(NlonN) but 최악의 경우(이미 정돈되어있음, pivot을 계속 맨 왼쪽만 or 맨 오른쪽만 선택) O(N^2)
- QuickSort, In-place QuickSort
- CountSort  
# 몰랐던 파이썬 문법
range(10,10 9 8 7 ... -1 -2 ...) : returns object containing empty list
range(10, 11) : returns object containing [10] 
for i in range(start, end, step = 1 or -1): step = -1일 때 index start부터 end+1까지 감소하며 반복
- sorted(), sort() 이용시 key 매개변수를 입력으로 받을 수 있음(key = ftn )
sorted(d.items(), key = lambda x:x[1]) -> values로 정렬, return은 튜플담은 리스트로
sorted(d.items(), key = lambda x:x[1], reverse = True) 내림차순
sorted(list with tuples, key = lambda x:x[1])
sorted(set) returns sorted list 
list.sort() (list 객체의 내장함수)

sum([1,2,3]) returns 6

