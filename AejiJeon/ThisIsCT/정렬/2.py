n = int(input())
seq = []
for _ in range(3):
    seq.append(int(input()))

print(*sorted(seq, reverse=True))