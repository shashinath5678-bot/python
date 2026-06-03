n = 4

i = 1
while i <= n:
    s = n - i
    while s > 0:
        print(" ", end="")
        s -= 1

    j = 1
    while j <= i:
        print(chr(64 + j), end="")
        j += 1

    j = i - 1
    while j >= 1:
        print(chr(64 + j), end="")
        j -= 1

    print()
    i += 1

i = n - 1
while i >= 1:
    s = n - i
    while s > 0:
        print(" ", end="")
        s -= 1

    j = 1
    while j <= i:
        print(chr(64 + j), end="")
        j += 1

    j = i - 1
    while j >= 1:
        print(chr(64 + j), end="")
        j -= 1

    print()
    i -= 1