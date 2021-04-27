A = list(str(input()))
B = list(str(input()))

# 배열 생성
arr = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
overlap = 0

#LCS
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            arr[j + 1][i + 1] = arr[j][i] + 1
            overlap = max(overlap, arr[j + 1][i + 1])

        else:
            arr[j + 1][i + 1] = max(arr[j][i + 1], arr[j + 1][i])

if len(B)-len(A) >=0:
    answer = len(B) -overlap
else:
    answer = len(A) - overlap

print(answer)

