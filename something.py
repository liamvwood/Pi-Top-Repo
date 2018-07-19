from gpiozero import LED
from time import sleep

led = LED(4)

def letterMorse(letter, led):
    if letter == 'a':
        dot(led)
        dash(led)
    elif letter == 'b':
        dash(led)
        dot(led)
        dot(led)
        dot(led)

word = input("Enter your message: ")
for letter in word:
    letterMorse(letter,led)