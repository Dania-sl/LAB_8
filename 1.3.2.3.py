import numpy as np
import timeit

while True:
    while True:
        try:
            shapeArray1 = int(input('enter shape of array 1: '))  # розмір списку 1
            shapeArray2 = int(input('enter shape of array 2: '))  # розмір списку 2
            break
        except ValueError:
            print('enter correct value')
    userArray1 = np.zeros(shapeArray1, dtype=int)  # створення нульового 1 списку розміром shapeArray
    userArray2 = np.zeros(shapeArray2, dtype=int)  # створення нульового 2 списку розміром shapeArray
    while True:
        try:
            for i in range(shapeArray1):
                userArray1[i] = int(
                    input(f'enter {i + 1} element first array: '))  # заповнення 1 списку рвндомними елементами
            for i in range(shapeArray2):
                userArray2[i] = int(
                    input(f'enter {i + 1} element second array: '))  # заповнення 2 списку рвндомними елементами
            break
        except ValueError:
            print('enter correct value')

    i = -1  # задання індексу елемента першого списку
    j = 0  # задання індексу елемента другого списку
    count = 0
    while j < len(userArray2) and i < (
            len(userArray1) - len(userArray2)):  # циклічне виконання доки індекс елементу другого списку менший за кількість елементів цього списку
        j = 0  # обнулення індексу порвняльного елементу
        i += 1  # наступний індекс елементу який порівнюється
        count += 2
        while j < len(userArray2) and userArray2[j] == userArray1[i + j]:  # циксічна перевірка елементів списку на рівність
            j += 1  # вибір індексу наступного елементу
            count += 2

    if j == len(userArray2):
        print(f'substring found in {i} position', count)
    else:
        print('element not found')
    time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('time:', time)
    if input('if you want continue, press Enter ') != '':
        break
