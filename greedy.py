def greedy(oddMoney):
    coins = [25, 10, 5, 1]
    cent = int(round(oddMoney*100))
    minCoins = 0
    n = 0
    while (cent > 0):
        if (cent >= coins[n]):
            cent -= coins[n]
            minCoins += 1
        else:
            n += 1
    print(minCoins)

while (True):
    oddMoney = float(input("How much change is owed?\n"))
    if (oddMoney > 0):
        greedy(oddMoney)
        break