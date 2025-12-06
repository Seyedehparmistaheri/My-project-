camel = input("name:")
s = ""
first = True

for i in camel:
    if i.isupper() and not first:
        s += "_" + i.lower()
    else:
        s += i.lower()
    first = False
print(s)
