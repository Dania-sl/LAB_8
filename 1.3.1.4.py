import numpy as np

while True:
    Matrix = np.zeros((4, 4), dtype=int)  # створення нульовї матриці розміром 4x4
    for i in range(4):
        for j in range(4):
            while True:
                try:
                    Matrix[i, j] = int(input(f'enter element  ({i + 1},{j + 1}) Matrix:'))  # заповнення матриці числами користувача
                    break
                except ValueError:
                    print('enter correct value')
    for i in range(4):
        for j in range(4):
            if Matrix[i][j] < 0:  # перевірка елементів
                Matrix[i][j] = 0  # заміна елементів < 0 на 0
    print(Matrix)
    if input('if you want continue, press Enter ') != '':
        break
