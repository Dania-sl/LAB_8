import numpy as np
import random
import timeit

while True:
    while True:
        try:
            shapeArray = int(input('Enter shape of array: '))  # розмір масиву
            userArray = np.zeros(shapeArray, dtype=int)  # створення нульового масиву розміром shapeArray
            searchingElement = int(input('Enter searching element: '))  # шуканий елемент
            break
        except ValueError:
            print('enter correct value')

    for i in range(shapeArray):
        userArray[i] = random.randint(0, 10)  # заповнення списку рвндомними елементами
    count = 0
    print(userArray)
    elementIndex = 0  # задання індекму елемента для пошуку
    lenArray = len(userArray)
    while elementIndex < lenArray and userArray[elementIndex] != searchingElement:  # перевірка на входження індексу елемнта в список
        elementIndex += 1
        count += 2
    if lenArray == elementIndex:  # перевірка на рівність кількості елементів в списку та індекс шуканого елементу
        print('no element')
    else:
        print(f'element {searchingElement} on {elementIndex}')  # якщо попередня перевірка не пройдена отже лемент є в списку під індексом
    time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('time:', time)
    if input('if you want continue, press Enter ') != '':
        break
