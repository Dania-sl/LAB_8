import numpy as np

while True:
    while True:
        try:
            userMatrix = np.zeros((3, 3), dtype=int)  # створення нульового масиву розміром 3x3
            finalMatrix = np.zeros((3, 3), dtype=int)  # створення нульового масиву розміром 3x3
            break
        except ValueError:
            print('enter correct value')

    for i in range(3):
        for j in range(3):

            while True:
                try:
                    userMatrix[i, j] = int(
                        input(f'enter element ({i + 1},{j + 1}):'))  # заповнення масиву числами користувача
                    break
                except ValueError:
                    print('enter correct value')

    print(userMatrix)
    for i in range(3):
        for j in range(3):
            finalMatrix[j][i] = userMatrix[i][j]  # заміна місуями рядків та стовбців
    print(finalMatrix)

    if input('if you want continue, press Enter ') != '':
        break
