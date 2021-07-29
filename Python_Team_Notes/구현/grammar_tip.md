# Python 문법 Tip들 모음집

## enumerate 특정 지점부터 시작

```python
 # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )
```



## set union, and intersection

```python
intersection = set(str1) & set(str2) # == set(str1).intersection(set(str2)) 
union = set(str1) | set(str2) # == set(str1).union(set(str2))
```



## Sorted 된 결과 바로 활용 및 key, reverse 사용법

```python
# sorted 자체가 iterable object임으로 for ~ in에 바로 활용하기
list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
```



##  두 set에서 최솟값 추출해서 바로 더하기

```python
# inline 활용하여 arr에 담고 sum으로 마무리
gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])
```

