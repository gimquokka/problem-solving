## 병사 배치하기(dp)
# 문제 요약
- n개 숫자 -> 내림차순 형태가 되는 가장 긴 부분 수열 찾기

# 아이디어
- dp문제에서 자주 등장하는 LIS(Longest Increasing Subsequence) '가장 긴 증가하는 부분 수열' 아이디어와 동일  
  
D[i] = array[j]를 마지막 원소로 가지는 부분 수열의 최대 길이
점화식: i = 1,2,...,n-1  
모든 0 <= j < i, 
    if array[j] < array[i],  
        D[i] = max(D[i], D[j] + 1)  
max(D) = LIS의 길이
