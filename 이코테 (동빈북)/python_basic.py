#=====================
#python basic practice
#=====================

'''
# remove all element in arrary not like a.remove
a = [1, 2, 2 , 3, 3, 3, 4, 5, 5, 5]
remove_set= {3, 5}

array = [i for i in a if i in remove_set]

print(array)
'''

'''
# 문자열 예시
string = "Hello World!"
print(string)

data = "Let's use \"python\""
print(data)

a = 'Hello'
b = 'World'

print(a + " " + b)
print(a*3)

a = "abcde"
print(a[:2])
'''

'''
# Tuple 사용법
a = (1, 2, 3, 4)
print(a)

a[2] = 1
'''

'''
# dictionary example
data = dict()
data['은지'] = '진영'
data['진영'] = '은지'
data['엄마'] = '아빠'
data['아빠'] = '엄마'

# if '엄마' in data:
#   print("엄마가 있다")

key_list = data.keys()
val_list = data.values()

print(key_list)
print(val_list)

for key in key_list:
  print(data[key])
'''

'''
#  ========== Set data example ========== 
data = set([1, 2, 3, 4, 5])
# print(data)

data = {1, 2, 3, 4, 5, 6, 7}
# print(data)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# print('합집합 a|b ', a|b)
# print('교집합 a&b ', a&b)
# print('차집합 a-b', a-b)

data = {1, 2, 3}

data.add(10)
data.update([1000, 100])
data.remove(5)

print(data)
'''

'''
# Condition
score = 80

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    pass

# print(True or False)
# print(not False)

grade = "pass" if score >= 60 else "fail"
print(grade)

a = [1, 2, 3, 4, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)
'''

"""
# Iteration
a = {1, 2, 3, 4}

# for i in a:
#   print(i)

scores = [90, 85, 40, 100]
cheating_list = {2, 4}

for i in range(4):
    if i + 1 in cheating_list:
        continue
    elif scores[i] >= 80:
        print(i+1, "번 학생은 Pass입니다.")
    else:
       print(i+1, "번 학생 fail입니다.")
"""

'''
# Function
def add(a, b):
  print(a+b)

add(1, 10)

a = 10; b =10

def func():
    global a, b
    print(a + b)

func()

print((lambda a, b: a + b)(1, 2))
'''

# Get input size
# n = int(input())

# Get input values
# a, b, c = map(int, input().split())
# # data = list(map(int, input().split(",")))

# print("n: ", n)
# print("data: ", a, b, c)

# import sys

# data = sys.stdin.readline().rstrip()

# a = 10
# print(f"문자열을 편한게 출력!{a}")

# Essential function
# result = sum({1, 2, 3})
# result = sum([1, 2, 3])
# result = min(1, 2, 3)
# result = max([1, 2, 3])
# result = eval("2**3 + 3*2")
# a = [2, 3, 1, 5, 8]
# a_sorted = sorted(a, reverse = True)
# print(a_sorted)

# result = sorted([(1, 2), (4, 5), (2, 1000), (0, 10)], key = lambda x: x[0])

# print(result)

# array = [1, 4, 2 ,3]

# array.sort()
# print(array)

'''
#itertools
from itertools import permutations, combinations, product, combinations_with_replacement

data = [1, 2, 3, 4]

result = list(permutations(data, 3))
result = list(combinations(data, 3))
result = list(product(data, repeat=2))
result = list(combinations_with_replacement(data, 2))

print(result)
'''

'''
# heapq library example
import heapq

def heapsort(iterable):
	h = []
	result = []
	# 모든 원소를 heap에 차례대로 삽입
	for val in iterable:
		heapq.heappush(h, -val)
	# 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
	for i in range(len(h)):
		result.append(-heapq.heappop(h))
	return result
a = [2, 3, 1, 5, 8, 2]

a_sorted= heapsort(a)
print(a_sorted)
'''

'''
# bisect lib example
from bisect import bisect_left, bisect_right

a = [1, 2, 2, 2, 2, 3, 4, 5]
x = 2

# print(bisect_left(a, x))
# print(bisect_right(a, x))

def count_by_range(iterable, left, right):
	right_index = bisect_right(iterable, right)
	left_index = bisect_left(iterable, left)
	return right_index - left_index

print(count_by_range(a, 2,2))
print(count_by_range(a, -1,2))
'''

'''
# collection lib ex
from collections import deque, Counter

data = deque([1, 2, 3, 4, 5])
# data.append(6)
# print(data.popleft())
# print(list(data))

counter = Counter(['a', 'a', 'b', 'c'])
print(counter['a'])
print(counter['b'])
print(counter['c'])

print(dict(counter))
'''

'''
# mathlib example
import math

print(math.factorial(3))
print(math.sqrt(4))
print(math.gcd(4, 12))
print(math.pi)
print(math.e)
'''
