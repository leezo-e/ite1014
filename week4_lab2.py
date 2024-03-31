while True :
    num = int(input("********\n1.Calculate\n2.Show it\n3.Initialize\n4.Quit\n********\ninput :"))

    if num == 1:
        a = int(input("Input the number : "))
        fib = [0, 1]
        for k in range(2,a+1) :
            fib.append(fib[k-1] + fib[k-2])
    elif num == 2:
        print(fib[k])
    elif num == 3:
        fib.clear()
    elif num == 4:
        break



