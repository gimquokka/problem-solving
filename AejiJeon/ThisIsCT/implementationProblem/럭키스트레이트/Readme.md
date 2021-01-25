# 실수한 부분
list에서 index slicing할 때 꼭 정수가 들어가야 함
'''python
l = 8
#lst1 = lst2[:l/2]  잘못된 표현 
lst1 = lst2[:l//2] 
'''