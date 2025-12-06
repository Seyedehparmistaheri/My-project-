m = input("vorodi ra bezanid:")
n = m.strip()
x , y ,z = n.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/":
    if y!=0:
        print (x/z)
    else:
        print("not allowed")
