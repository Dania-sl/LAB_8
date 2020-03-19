import numpy as np

while True:
    while True:
        try:
            shapeArray = int(input('enter shape of array: '))  # розмір масиву
            break
        except ValueError:
            print('enter correct value')

    userArray = np.zeros(shapeArray, dtype=int)  # створення нульового масиву розміром shapeArray
    for i in range(shapeArray):
        num_of_element = i + 1
        while True:
            try:
                userArray[i] = int(
                    input(f'enter element number {num_of_element}: '))  # заповнення масиву числами користувача
                break
            except ValueError:
                print('enter correct value')
    print(userArray[::-1])  # задання оберненого відображення масиву
    if input('if you want continue, press Enter ') != '':
        break
