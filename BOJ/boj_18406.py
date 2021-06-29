n = input()
print("LUCKY" if sum(map(int, n[:len(n)//2]))== sum(map(int, n[len(n)//2:])) else "READY")
