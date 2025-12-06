i = {}

while True:
    try:
        item = input()
        t = item.upper()
        if t in i:
            i[t] += 1
        else:
            i[t] = 1

            continue
    except EOFError:
        for s in sorted(i.keys()):
            print(f"{i[s]} {s}")

        break
