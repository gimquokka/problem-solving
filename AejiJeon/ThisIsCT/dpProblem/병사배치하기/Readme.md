# 병사 배치하기(dynamic programming)
## 문제 요약
- n개 숫자 -> 내림차순 형태가 되는 가장 긴 부분 수열 찾기

## 아이디어
- dp문제에서 자주 등장하는 LIS(Longest Increasing Subsequence) '가장 긴 증가하는 부분 수열' 아이디어와 동일  

점화식:  
D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이  
i = 1,2,...,n-1  
모든 0 <= j < i, 
    if array[j] < array[i],  
        D[i] = max(D[j] + 1, D[i])  
max(D) = LIS의 길이
