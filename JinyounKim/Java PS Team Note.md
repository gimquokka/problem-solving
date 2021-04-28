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

- 자바에서는 파이썬과 같이 "String" == "String"을 하면 안됨

```java
// 객체는 그냥 부르면 주소 값을 뱉음으로 == 비교 불가능
(X) "String" == "String"

// 아래와 같이 String의 내부 method를 활용하여 비교를 수행하여야함
"String".equals("String")
```

- DFS 사용시 visited 사용 Pattern

```java
        for (int i = 0; i < words.length; i++) {
            if (!visited[i] && check(begin, words[i])) {
                //해당 DFS로 진입할 때 visited 처리
              	visited[i] = true;
                dfs(words, words[i], target, cnt + 1);
                // 다음 차례의 dfs의 경로는 해당 node를 다시 방문해야할 수 있음으로 방문 기록 지워줘야함
                visited[i] = false;
            }
        }
```

- Fibonacci 제귀함수 구현 Best Practice

```java
import java.util.Scanner;

public class Quiz11_04 {
    static int n;
    static int arr[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
				
      	// n 받아서, 여기까지의 피보나치 수 구하여랴!
        n = sc.nextInt();
        arr = new int[n+1];

        arr[1] = 1;
        arr[2] = 2;

        f(n);

        System.out.println(arr[n]);
    }

    private static int f(int n) {
        if (arr[n] == 0) return arr[n] = f(n - 1) + f(n - 2);
        return arr[n];
    }
}
```

- Binary Search

```java
public static int binarySearch(int[] list, int key){
  int low = 0;
  int list.length - 1;
  
  while(high >= low){
    int mid = (low + high) / 2;
    if (key > list[mid]) 
      low = mid +1;
    else if (key == list[mid])
      return mid;
    else
      high = mid - 1;
  }
  return - 1 - low; 
}
```

- Queue

```java
// 라이브러리 import
import java.util.LinkedList;
import java.util.Queue;

// LinkedList를 활용하여 Queue 초기화
Queue<Integer> q = new LinkedList<>(); // Integer 말고도 다른 DataType Generic으로 사용가능

// 삽입 (Create)
q.add(1); // 삽입에 성공시 true, 실패하였을 경우 Exception 반환 
q.offer(2); // 삽입에 성공시 true, 실패하였을 경우 false 반환 

// 참조 (Read)
queue.peek(); // Queue의 첫번째 값 참조

// 반환 (Read and Delete)
q.poll(); // Queue의 첫번째 값을 반환. 비어있다면 null 반환


// 제거 (Delete)
q.remove(); // Queue의 첫번째 값 제거
q.clear(); // Queue의 값 초기화
```

