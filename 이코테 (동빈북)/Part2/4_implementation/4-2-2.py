n = int(input())

ans = 0
for hh in range(n+1):
    for mm in range(60):
        for ss in range(60):
            if '3' in str(hh)+str(mm)+str(ss):
                ans += 1

print(ans)
