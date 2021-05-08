- enumerate 특정 지점부터 시작

```python
 # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )
```

