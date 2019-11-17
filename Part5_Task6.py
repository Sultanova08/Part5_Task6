def abbreviation(a, b):
    if len(b) == 0:
        return len(a) == 0 or a.islower()  # no more uppercase
    elif len(a) == 0:
        return False
    else:
        if a[0].islower():
            if abbreviation(a[1:], b):
                return True
        if a[0].upper() == b[0]:
            if abbreviation(a[1:], b[1:]):
                return True
        return False

q = int(input("Enter the number of the steps:"))
for _ in range(q):
    a = input("Enter the mixed strings: ")
    b = input("Enter the strings: ")
    print('YES' if abbreviation(a, b) else 'NO')