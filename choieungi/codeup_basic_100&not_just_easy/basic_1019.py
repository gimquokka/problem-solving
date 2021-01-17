a = input("")
b= a.split(".")
print("%04d.%02d.%02d" %(int(b[0]), int(b[1]), int(b[2])) )

# %d에서 %02d를 사용하면 한자리수를 넣어도 두자리수 형식이 출력 ex) 2 --> 02 출력
# %가 많을때 print("%d %d %d" %(a,b,c))

