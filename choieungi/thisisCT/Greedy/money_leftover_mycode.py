def leftover_cash(money):
    moneys = [10, 50, 100, 500]
    coin = 0
    moneys.sort(reverse=True)
    for i in moneys:   #역순 정렬
        coin += money//i
        money = money%i
    return coin

print(leftover_cash(1260))