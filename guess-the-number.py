import random
answer = random.randint(1,1001)
gameOver = False
while not gameOver:
    guess = int(input("Enter your guess (between 1 and 1001): "))
    if guess == answer:
        print ("You guessed right!")
        gameOver = True
    elif guess > answer:
        print ("Too high, dude")
    else:
        print ("Too low, dude")
