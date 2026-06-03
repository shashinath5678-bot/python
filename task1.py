rows = 5

i = 1
while i <= rows:
    space = rows - i
    while space > 0:
        print(" ", end="")
        space = space - 1

    star = 1
    while star <= (2 * i - 1):
        print("*", end="")
        star = star + 1

    print()
    i = i + 1