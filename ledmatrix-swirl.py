from gpiozero import ledmatrix
from time import sleep

def checkNext(x,y):
    if x == 7 or x == -1:
        return False
    elif y == 7 or y == -1:
        return False
    elif ledmatrix.get_pixel(x,y) == (0,0,255):
        return False
    else:
        return True
x = 0
y = 0

def moveUp():
    y = y + 1
def moveRight():
    x = x + 1
def moveDown():
    y = y - 1
def moveLeft():
    x = x - 1

moves = [moveUp, moveRight, moveDown, moveLeft]
i = 0
while True:
    moves[i]()
    ledmatrix.set_pixel(x,y,0,0,255)
    ledmatrix.show()
    sleep(1)
    if not checkNext():
        i + 1
        if i == 4:
            i = 0