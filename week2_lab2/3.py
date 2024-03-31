spacenum = 4
star = 1

for i in range(9):
    print(" "*spacenum, "*"*star)
    if i < 4 :
        spacenum -= 1
        star += 2
    else :
        spacenum += 1
        star -= 2

