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

