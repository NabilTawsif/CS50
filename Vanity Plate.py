def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num_found = 0
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for i in range(2, len(s) - 1):
                if s[i].isalpha():
                    continue
                if s[i].isnumeric():
                    num_found = i
                    break
            if num_found == 0:
                return True
            s = s.split(s[num_found - 1])
            if s[ len(s) - 1 ].isnumeric():
                s = s[ len(s) - 1 ]
                if len(s) == len(str(int(s))):
                    return True
                return False
            return False
        return False
    return False

main()