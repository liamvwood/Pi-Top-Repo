import random

number_of_tries = 0
while number_of_tries < 10:
    first_number = random.randint(0,200)
    second_number = random.randint(0,200)

    answer = first_number + second_number

    guess_correct = False
    number_of_guesses = 0

    while not guess_correct and number_of_guesses < 3:

        guess = input(str(first_number) + " + " + str(second_number) + " = ")

        if guess == str(answer):
            print("CORRECT!!!")
            guess_correct = True
        else:
            number_of_guesses = number_of_guesses + 1
            print("Ooooops! Try again!!!")
    number_of_tries = number_of_tries + 1
