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
        userArray[i] = random.randint(0, 10)  # заповнення списку рандомними елементами
    userArray.sort()  # сортування списку за зростанням
    print(userArray)
    leftLimit = 0  # встановлення лівої границі
    rightLimit = len(userArray)  # встановлення правої границі

    while leftLimit < rightLimit - 1:
        mid = (leftLimit + rightLimit) // 2  # знаходження індексу середнього елементу
        if userArray[mid] > searchingElement:  # порівння елементу під індексом mid з шуканим елементом
            rightLimit = mid  # пересування правлї границі на позицію mid
        else:
            leftLimit = mid  # пересунення лівої границі на позицію mid
    if leftLimit >= 0 and userArray[leftLimit] == searchingElement:  # перевірка елементу на входження в список
        print(leftLimit)
    else:
        print('no element')
    time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('time:', time)
    if input('if you want continue, press Enter ') != '':
        break
