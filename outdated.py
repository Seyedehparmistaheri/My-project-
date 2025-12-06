m ={"january":1,

"february":2,

"march":3,

"april":4,

"may":5,

"june":6,

"july":7,

"august":8,

"september":9,

"october":10,

"november":11,

"december":12
}

while True:

    t = input("Date: ")

    if "/" in t:

        try:

            month, day, year = t.split("/")

            month = int(month)

            day = int(day)

            year = int(year)

        except ValueError:

            continue
    else:

        if "," not in t:

            continue
        try:

            monthi, day, year = t.replace(",", "").split()

            if monthi.lower() not in m:
                  continue

            month = m[monthi.lower()]

            day = int(day)

            year = int(year)

        except ValueError:

            continue

    if not (1 <= month <= 12 and 1 <= day <= 31):

        continue

    print(f"{year:04}-{month:02}-{day:02}")

    break
