# 효율적인 풀이
너무 복잡하게 품.. 문제에서 말한대로 string 압축 후 압축한 stringd의 length를 비교하면 됨.

# 몰랐던 python 기능, 문법
- string, array에서 index slicing할 때 outofindex에서 추출해도 error안남
'''python
a = 'abc'
b = [1,2,3]
print(a[2:7]) # 'c' printed
print(b[1:10]) # [2,3] printd
print(a[-1:5]) # 'c' printed
print(b[-5:5]) # [1,2,3] printed
'''