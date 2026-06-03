n = 5

i = 1
while i <= n:

    spaces = n - i
    while spaces > 0:
        print(" ", end="")
        spaces = spaces - 1

    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1

    print()
    i = i + 1