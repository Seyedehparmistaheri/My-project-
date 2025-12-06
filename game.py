import random

while  True:
    try:
        n = int(input("Level: " ))
    except ValueError:
        continue
    if n <= 0:
        continue
    m = random.randint(1, n)
    while True:
        guess = input("Guess: ")
        try:
            g = int(guess)
            if g < 1:
                continue
        except ValueError:
            continue

        if g < m:
            print("Too small!")
            continue
        elif g > m:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    break

