def main():
    p, n, h = map(int, input().split())

    pc_list = [0]*(p+1)
    for i in range(n):
        pc_num, hour = map(int, input().split())
        if hour > h:
            continue
        if hour <= h:
            pc_list[pc_num] += hour
    for i in range(1, p+1):
        if pc_list[i] > h:
            print(i, h*1000)
        else:
            print(i, pc_list[i]*1000)

if __name__=="__main__":
    main()