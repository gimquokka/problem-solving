# 효율적인 풀이
print(''.join(alphabet)+str(numbers_sum))
# 몰랐던 python 기능
'''python
a = 'bfaecd'
a = sorted(a)  # string에는 sort() ftn 적용시킬 수 x
print(a)     # ['a', 'b', 'c', 'd', 'e', 'f'] printed 즉, sorted(iterable object) -> sort후 list로 return
'''
- string의 isalpha() 함수  
'''python  
if 'a'.isalpha(): # True값 return
    print("It is alphabet.")
'''
str(123) : '123' 
chr(123) : '{' (ascii) 