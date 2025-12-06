while True:
    try:
        s = input("x/y:")
        t,u = s.split("/")
        x = int(t)
        y = int(u)
        m =round(x/y*100)
        if m < 0:
            continue

        elif m <= 1:
            print("E")
        elif m > 100:
            continue

        elif m >= 99:
            print("F")

        else:
            print(f"{m}%")
        break

    except ValueError:
        print("x or y is not an integer")
    except ZeroDivisionError:
        print("y should not be 0")
    continue
