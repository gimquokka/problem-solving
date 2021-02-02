# 최종순위
https://www.acmicpc.net/problem/3665

## Trouble shooting
### 그래프에 cycle이 있는지 없는지 판단 하는 방법
- result배열과 node의 개수를 비교함
    - result배열이 더 짧으면, cycle이 발생한 것임. 왜냐면 cycle은 result배열에 포함될 수 없기 때문임!!!!!