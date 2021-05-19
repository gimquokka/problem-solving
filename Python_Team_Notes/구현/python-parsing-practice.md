# Python Parsing Practice

## 문자열의 숫자 개수만 dict으로 추출하기

```python
number_cnt = Counter(re.findall('\d+', string))
```

## 모든 alphabet 대/소문자로 변경

```python
# 소문자로 변경
string.lower()

# 대문자로 변경
string.upper()
```

## 문자열이 alphabet 혹은 숫자로만 이루어졌는지 판별

```python
# alphabet으로만 이루어졌는지 판별
"abcd".isalpha() # True
"ab2d".isalpha() # False

# 숫자로만 이루어졌는지 판별
"123".isdigit() # True
"ab123".isdigit() # False

# alphabet 혹은 숫자로 이루어졌는지 판별
"123abc".isalnum() # True
"123##ab".isalnum() # False
```

## 정규식 예시들

전체 내용은 아래의 링크를 참조. 실제 문제에서 겪은 예시만 정리

[잘 정리된 문서](https://wikidocs.net/4308#_2)

```python
import re
from collections import Counter

# alphabet이 아닌 문자가 문자열에 포함되어 있는지 반환
string = "12 #abc# 123"
result = re.findall('[^a-zA-Z]+', string)
print(result) # ['12 #', '# 123']

# 문자열에서 나타나는 숫자와 개수를 dict 형태로 반환
string = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
result = Counter(re.findall('\d+', string))
print(result) # Counter({'2': 4, '1': 3, '3': 2, '4': 1})



```

