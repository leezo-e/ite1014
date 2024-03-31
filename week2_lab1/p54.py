for line in range (1,6):
    for star1 in range (0, (5-line)*2):
        print(' ', end="")
    for star2 in range (1, line*2):
        print('*', end = "")

    print ()