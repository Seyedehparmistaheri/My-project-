k = {
 "baja taco": 4.00,

"burrito": 7.50,

"bowl": 8.50,

"nachos": 11.00,

"quesadilla": 8.50,

"super burrito": 8.75,

"super quesadilla": 9.50,

"taco": 3.00,

"tortilla salad": 8.00
 }
T = 0
while True:
    try:
        s = input("Item: ")
        n = s.lower()
        if n in k:
            p = k[n]
            T += float(p)
            print(f"${T:.2f}")
            continue
        elif  n not in k:
            continue

    except EOFError:
        print("finish")
    break
