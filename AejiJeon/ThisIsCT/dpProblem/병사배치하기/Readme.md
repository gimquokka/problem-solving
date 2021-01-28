# 풀이
LIS(Longest Increasing Subsequence)로 알려진 전형적인 DP 문제의 아이디어 사용
DP 점화식 : D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이 -> 모든 0 <= j < i에 대하여, D[i] = max(D[i],D[j] + 1) if array[j] < array[i] (DP 테이블의 값은 모두 1로 초기화) i = 1부터 n-1까지 진행 -> 최종적 테이블에 남아 있는 값 중에서 가장 큰 값이 LIS(Longest Increasing Subsequence)의 길이가 됨