def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    for x in range(n):
        for y in range(m):
            arr1[x][y] += arr2[x][y]
    return arr1

'''
# 짧은 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))

'''