# Java PS Team Note

- 최대공약수 (GCD)

  ```java
  // Without library
  public int gcd(int a, int b) 
  { return b==0 ? a : gcd(b, a%b); }
  
  // With built-in library
  gcd = BigInteger.valuOf(a).gcd(BigInteger.valuoOf(b)).intValue();
  ```

- 문자열 복사

```java
Optional<String> result = Stream.generate(() -> "*").limit(i%(n+1)).reduce((a, b) -> a + b);
            System.out.println(result.get()) ;
```

- Char array => String

```java
String stringRef= String.valueOf(charArray)
```

- Sort reference type array

``` java
// 기본 오름차순 정렬은 {premitiveType, String}만 지원

// startIdx ~ (endIdx-1)의 구간만 정렬
Arrays.sort(typeArr, startIdx, endIdx)
  
// comparator가 -1가 되도록 정렬 (레퍼런스 type만 해당함)
// 1. 오름차순
Arrays.sort(typeArr, (o1, o2) -> o1 - o2)
// 2. 내림차순
Arrays.sort(typeArr, (o1, o2) -> o2 - o1)
```

- Retrive value in Map

```java
 	// 찾는 키가 존재한다면 찾는 키의 값을 반환하고 없다면 기본 값을 반환한다.
	map.getOrDefault(Object key, V defaultValue)
  
  // 사용 예시
  Map<String, Integer> map = new HashMap<>();
  for (String key : combination) {
    map.put(key, map.getOrDefault(key, 0) + 1);
  }
```

- List => String Array

```java
List<String> ansList = new ArrayList<>();
....
// Convert arrayList => String[]  
String[] answer = new String[ansList.size()];
ansList.toArray(answer);
```

- List (arrayList, linkedList, ...) Collections 소속 클레스 기본 정렬

```java
// Return Type void
Collections.sort(List);
```

- Char[] => String

```java
String str = String.valueOf(charArray)
```

- 파이썬에서 1 in [1, 2 ,3]과 같이 포함여부 확인하는 기능

```java
String[] values = {"AB","BC","CD","AE"};
boolean contains = Arrays.stream(values).anyMatch(x -> x == equals);
```

