def refund(n):
    r500, remain = divmod(n, 500)
    r100, remain = divmod(remain, 100)
    r50, remain = divmod(remain, 50)
    r10, _ = divmod(remain, 10)
    
    return r10+r50+r100+r500


print(refund(1000))
    