
#code 1 list comprehension

array = [i for i in range(20)]

print(array)

#code 2 normal code

array = []
for i in range(20):
    array.append(i)

print(array)

# 중요 list comprehension은 2차원 리스트 초기화에서 효과적으로 사용 특히 N X M 크기 리스트
N,M = 10,10 #10X10 이차원 배열 n은 행 m은 열 유튜브 55분
array=[[0]*M for _ in range (N)]
print(array)

# 반복문에서 _는 반복을 위한 변수의 값을 무시할 때 사용

#리스트 관련 함수
a=[1,2,3,4]
a.insert(2,3) #인덱스가 2인 곳에 3을 추가
a.remove(1) #값이 1인 데이터 제거 (여러개일 경우 한개만 제거)

#리스트에서 특정 값을 갖는 원소를 모두 제거하기 --> 집합 set 이
a=[1,2,3,4,5,5,5,6,7,]
remove_set = {3,5}
result = [i for i in a if i not in remove_set]



#튜플은 메모리 이득, 서로 다른 성질 데이터 관리(최단 경로), 데이터 나열(hashing의 키값)용--> 파이썬에서는 딕셔너리 자료형이
#hashing을 이용