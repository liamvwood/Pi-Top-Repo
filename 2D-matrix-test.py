from ptpulse import ledmatrix
letter_a = [[0] * 7 for i in range(7)]

letter_a[1][1] = 1

for i in range(7):
    for j in range(7):
        if letter_a[i][j] is not 0:
            ledmatrix.set_pixel(i,j,255,255,255)

ledmatrix.show()