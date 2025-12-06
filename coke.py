coke = 50
while coke > 0:
    coins = [25,10,5]
    v = int(input("insert_coin:"))
    if v in coins:
        coke = coke - v
        print(f"Amount Due: {coke}")
    else:
        print("Amount Due: 50")




save = abs(coke)
print(f"Change Owed: {save}")
