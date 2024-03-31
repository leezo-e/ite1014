print("단수를 입력하시오 :")
num = int(input())

if num < 2 or num > 9:
    print("잘못된 입력범위입니다.")
else:
    for a in range(1, 10):
        print("%i * %i = %i " % (num, a, num * a))




