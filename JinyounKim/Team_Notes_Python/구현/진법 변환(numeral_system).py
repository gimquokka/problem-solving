# 진법변환
# 1. 10진법을 넘어가는 경우
def numeral_system(number, base):
    # Incase of base = 3. If base = 16? NOTATION = '0123456789ABCDEF'
    NOTATION = '012'
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base)+n if q else n


# 2. 10진법 안쪽인 경우
while n:
    tmp += str(n % 3) + tmp
    n = n // base

# 3. base진법을 10진법으로 바꾸는 경우
int(tmp, 3)
