N = int(input("Enter the number of lines :"))

for line in range(1, N+1):
    for stars in range (1, line*2):
        print ('*', end = "")
    print()

    