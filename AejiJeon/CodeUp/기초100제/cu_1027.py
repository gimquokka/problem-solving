# date -> day, month, year
year, month, day = input().split(".")
print("%02d-%02d-%04d" %(int(day), int(month), int(year)))