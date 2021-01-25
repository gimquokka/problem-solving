# 효율적인 풀이
무게 <= 10 -> list 만들어서 해당 무게를 가지는 볼링공 개수 저장, 무게 저장한 list 가지고 무게 낮은 볼링공부터 높은 볼링공까지 순서대로 하나씩 확인

# 실수한 부분
lst1 = lst2.sort() (x) sort() ftn은 sort된 list 객체를 return하지 않음.

'''python
lst1 = lst2  
lst1.sort()
'''