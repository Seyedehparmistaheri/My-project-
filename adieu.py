import inflect
p = inflect.engine()


#get names
names = []

while True:
    try:
        n = input()
        names.append(n)
        h = p.join(names)
        continue
    except EOFError:
        print(f"Adieu, adieu, to {h}")
        break
