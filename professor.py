import random

def main():
    level = get_level()
    j = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        h = x + y

        maxt = 3
        t = 0
        while t < maxt:
            c = input(f"{x} + {y} =")
            try:
                c = int(c)
            except ValueError:
                print("EEE")
                t += 1
                continue
            if c == h:
                j += 1
                break
            else:
                print("EEE")
                t += 1
        if t == maxt:
            print(h)
    print("Score: ", j)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level in [1,2,3]:
            return level
        else:
            print("level number is not in the range")
            continue




def generate_integer(level):
    if level == 1:
        return random.randint(0,9)

    elif level == 2:
        return random.randint(10,99)

    elif level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
