a1 = -4

n = int(input("Enter the number, n:"))

for k in range (1,n):
    a2 = 2*a1 + 5
    print ("a(%i) = %i." %(k+1, a2))

    a1 = a2

    print ("Final answer of a(%i) = %i" %(n,a2))

