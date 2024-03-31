import random

hist0 = hist1 = hist2 = hist3 = hist4 = 0

for k in range (100):
    num = random.randint(1,100)
    if num%5 == 0 :
        hist0 += 1
    elif num%5 == 1 :
        hist1 += 1
    elif num%5 == 2 :
        hist2 += 1
    elif num%5 == 3 :
        hist3 += 1
    else :
        hist4 += 1

    print("Current iteration is %i."%(k+1))

print("The numbers of remainders :", hist0, hist1, hist2, hist3, hist4)
