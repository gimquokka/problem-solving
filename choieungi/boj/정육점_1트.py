n,m= map(int,input().split())
meat =[0]*(n)

for i in range(n):
    a,b =map(int,input().split())
    meat[i] =(a,b)

meat.sort(key=lambda x:(x[1],-x[0]))

max_amount={}
sum_amount={}

for i,j in meat:
    try:
        sum_amount[j] += i
    except:
        sum_amount[j] = i
    try:
        max_amount[j] = max(max_amount[j],i)
    except:
        max_amount[j]=i

#print(max_amount,sum_amount)


max_amounts = sorted(max_amount.items())
sum_amounts = sorted(sum_amount.items())


sum=0
k=0
#print(sum_amounts)
#print(max_amounts)
for i,j in sum_amounts:
    if i == sum_amounts[0][0]:
        amount = max_amounts[0][1]
    else:
        amount = max_amounts[k][1] + sum
    sum +=j

    price =i
    k+=1
    if amount>= m:
        break



if amount<m:
    print(-1)
else:
    print(price)


'''
amount = 0
index=[0]*n
for i,j in enumerate(meat):
    amount += j[1]
    price = j[0]
    index[i] =i


    if amount >=m:
        if index[i]-index[i-1] >0 and price[i]==price[i-1]:
            price+=1

'''
