# 효율적인 풀이
- dequq() ftn import 없이 그냥 list로 queue 기능 간단하게 구현 가능
q.append(), q.pop(0)
# 몰랐던 python 기능
'''python
a = [-2,-1,0,1,2,3,4,5]
for i in range(a):
    print(a%3, end = ' ') # 1 2 0 1 2 0 1 2 printed (음수 나눌 때도 이어짐)
'''