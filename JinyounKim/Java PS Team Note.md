# Java PS Team Note

- 최대공약수 (GCD)

  ```java
  // Without library
  public int gcd(int a, int b) 
  { return b==0 ? a : gcd(b, a%b); }
  
  // With built-in library
  gcd = BigInteger.valuOf(a).gcd(BigInteger.valuoOf(b)).intValue();
  ```

- ?