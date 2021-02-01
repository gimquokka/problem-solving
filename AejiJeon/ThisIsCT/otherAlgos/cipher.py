# cipher 사이펄
from itertools import combinations

l, c = map(int, input().split())

alphabets = input().split()
alphabets.sort()

vowel = ['a', 'e', 'i', 'o', 'u']
# ('a', 'b', 'c', 'd')
for comb in combinations(alphabets, l):
    vower_count = 0
    for  c in comb:
        if c in vowel:
            vower_count += 1
    if 1 <= vower_count <= l-2:
        print("".join(comb))

