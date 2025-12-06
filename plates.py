
def main():
    plate = input("Plate:").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False
    first_digit_index = None
    for i, ch in enumerate(s):
        if ch.isdigit():
            first_digit_index = i
            break
    if first_digit_index is not None:
        for ch in s[first_digit_index:]:
            if not ch.isdigit():
                return False
        if s[first_digit_index] == "0":
            return False
    return True

main()
