import random
secret = random.randint(1,99)
guess = 0
tries = 0

while guess != secret and tries <6:
    guess = int(input("What's your guess?"))
    if guess < secret:
        print("Too low!")
    elif guess > secret :
        print("Too high!")
    tries = tries + 1

if guess == secret :
    print ("You got it! Found my secret, you did!")
else :
    print ("No more guesses!", "The secret number was", secret)