import numpy as np

while True:
    while True:
        try:
            row_firstMatrix = int(input('Enter amount rows in first matrix: '))  # рядки матриці 1
            col_firstMatrix = int(input('Enter amount columns in first matrix: '))  # строки матриці 1
            row_secondMatrix = int(input('Enter amount rows in second matrix: '))   # рядки матриці 2
            col_secondMatrix = int(input('Enter amount columns in second matrix: '))  # строки матриці 2
            if col_firstMatrix == row_secondMatrix:  # перевірка матриць на сувмісність
                break
            else:
                print('amount columns in first matrix not equal amount rows in second matrix')
        except ValueError:
            print('enter correct value')

    firstMatrix = np.zeros((row_firstMatrix, col_firstMatrix), dtype=int)  # створення нульового масиву розміром 3x3
    for i in range(row_firstMatrix):
        for j in range(col_firstMatrix):
            while True:
                try:
                    firstMatrix[i, j] = int(input(f'enter element  ({i + 1},{j + 1}) first Matrix:'))  # заповнення масиву числами користувача
                    break
                except ValueError:
                    print('enter correct value')

    secondMatrix = np.zeros((row_secondMatrix, col_secondMatrix), dtype=int)  # створення нульового масиву розміром 3x3
    for i in range(row_secondMatrix):
        for j in range(col_secondMatrix):
            while True:
                try:
                    secondMatrix[i, j] = int(input(f'enter element ({i + 1},{j + 1}) second Matrix:'))  # заповнення матриці числами користувача
                    break
                except ValueError:
                    print('enter correct value')

    new_element = 0  # елемент нової матриці
    bufferMatrix = []
    finalMatrix = []
    for z in range(0, row_firstMatrix):  # рядок першої матриці
        for j in range(0, col_secondMatrix):  # стовпчик другої матриці
            for i in range(0, col_firstMatrix):  # рядок другої та стовбець першої
                new_element = new_element + firstMatrix[z][i] * secondMatrix[i][j]  # підрахунок нового елементу матрриці
            bufferMatrix.append(new_element)  # додання новгого елементу в буферну матрицю
            new_element = 0  # обнулення нового елементу для подальшого пошуку інших
        finalMatrix.append(bufferMatrix)  # додання елементу з буферної матриці в кінцеву
        bufferMatrix = []  # обнулення буферної матриці
    print(finalMatrix)
    if input('if you want continue, press Enter ') != '':
        break
