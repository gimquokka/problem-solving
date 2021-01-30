string_a = input()
string_b = input()

n = len(string_a)
m = len(string_b)

mat = [[0]*(m+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if string_a[i-1] == string_b[j-1]:
            mat[i][j] = mat[i-1][j-1]+1
        else:
            mat[i][j] = max(mat[i-1][j], mat[i][j-1])

substring = ''

i, j = n, m

while mat[i][j] != 0:
    if string_a[i-1] == string_b[j-1]:
        substring += string_a[i-1]
        i -= 1
        j -= 1
    
    elif mat[i][j] == mat[i][j-1]:
        j -= 1
    else:
        i -= 1
substring = substring[::-1]

i, j, k = 0, 0, 0
count = 0
while i != len(string_a) or j != len(string_b) or k != len(substring):
    a, b, s = string_a[i], string_b[j], substring[k]
    if a == s and b == s: # 패스
        i += 1
        j += 1
        k += 1
        continue
    elif a == s and b != s: # 삽입
        
        j += 1
    
    elif a != s and b == s:#삭제
        i += 1
    else: # 교체
        
        i += 1
        j += 1
    
    count += 1

print(count)



