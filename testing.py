import random
while True:
    first_number = random.randint(0,200)
    second_number = random.randint(0,200)

    answer = first_number + second_number

    guess_correct = False
    number_of_guesses = 0
    while not guess_correct and number_of_guesses < 3:
        guess = input(str(first_number) + " + " + str(second_number) + " = ")

        if guess == str(answer):
            print("Correct!")
            guess_correct = True
        else:
            print("Ooops! Guess again!")
            number_of_guesses = number_of_guesses + 1



