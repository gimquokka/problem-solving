# integer -> sizes of digits
integer = input()
i=4
for a in integer:
    print("[%d]" %(int(a)*pow(10,i)))
    i -= 1
