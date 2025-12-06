deep = input("javaba:")
A = deep.lower().strip()
if A == '42':
    print("yes")
elif A == 'forty-two':
    print("yes")
elif A == 'forty two':
    print("yes")

else:
    print("No")
