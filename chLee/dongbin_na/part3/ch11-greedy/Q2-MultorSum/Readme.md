# 곱하기 혹은 더하기

## Solution
1. 왼쪽부터 두 숫자 씩 연산을 한다 (sliding window - size 2)
    - 기본적으로 모든 연산은 `x`연산
    - 만일 두 수 중 적어도 하나가 0또는 1이라면, `+`연산
2. 연산 결과를 window 오른쪽에 배치  
3. window의 오른쪽 원소가 `\0(null)`일 때 까지 1,2반복

## Solution - official
- 0또는 1일때만 더하기를 한다는 생각은 똑같음. 다만, result에 첫 숫자를 넣어놓고 index 1부터 계산을 시작한다는 것이 다름
- **result가 long long이 되야 함**