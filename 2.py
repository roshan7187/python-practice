n = 5
#Upper Half of diamond
# outer loop for rows
for i in range(n):

    # spaces before stars
    for j in range(n - i - 1):
        print(" ", end="")

    # stars
    for j in range(2 * i + 1):
        print("*", end="")

    # spaces after stars
    for j in range(n - i - 1):
        print(" ", end="")

    # next line
    print()


#Lower Half of diamond
# outer loop for rows
for i in range(n,0,-1):

    # spaces before stars
    for j in range(0, n - i):
        print(" ", end="")

    # stars
    for j in range(2 * i - 1):
        print("*", end="")

    # spaces after stars
    for j in range(0, n - i):
        print(" ", end="")

    # next line
    print()
#rows = 5