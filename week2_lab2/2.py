passed=failed=0
for i in range(1,11):
    a=int(input("Enter result (1 = pass, 2 = fail)"))

    if a == 1 :
        passed += 1
    elif a == 2 :
        failed += 1
print ("pass = %i failed = %i" %(passed,failed))