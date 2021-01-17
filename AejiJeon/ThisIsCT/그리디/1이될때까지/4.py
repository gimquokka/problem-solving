
n, k = map(int, input().split())

result = 0

while True:
    n_k = (n // k) * k  #k로 나눌 부분
    result += n - n_k   #k로 나누기 전까지 뺀 횟수
    n = n_k

    if n < k:
        result += n - 1 #마지막 뺀 횟수 더하기
        break

    n //= k
    result += 1



print(result)