'''
Інформація про кількість деталей на автоматизованому складі зберігається в
комп'ютері; номенклатура деталей визначається розміром і кольором. Скласти
програму, яка виводить на екран вибіркові відомості про кількість усіх деталей заданої
номенклатури, а також, при бажанні, про терміни і кількості надходжень деталей цієї
номенклатури в відповідних партіях. Якщо деталі даної номенклатури відсутні на складі,
або сталася помилка при введенні номенклатури, то про це програма повинна
повідомляти оператору.
'''
import numpy as np
import datetime

while True:
    flag = False
    p1 = np.array([{'detail': 'gears', 'amount': 23, 'term': datetime.date(2020, 3, 23), 'color': 'grey', 'size': 15},
                   {'detail': 'bolts', 'amount': 100, 'term': datetime.date(2020, 3, 24), 'color': 'black', 'size': 10},
                   {'detail': 'nuts', 'amount': 85, 'term': datetime.date(2020, 3, 22), 'color': 'white', 'size': 15},
                   {'detail': 'washers', 'amount': 50, 'term': datetime.date(2020, 3, 23), 'color': 'red',
                    'size': 20}])  # перша партія деталей
    p2 = np.array([{'detail': 'gears', 'amount': 34, 'term': datetime.date(2020, 2, 23), 'color': 'grey', 'size': 15},
                   {'detail': 'bolts', 'amount': 83, 'term': datetime.date(2020, 2, 22), 'color': 'black', 'size': 10},
                   {'detail': 'nuts', 'amount': 20, 'term': datetime.date(2020, 2, 24), 'color': 'white', 'size': 15},
                   {'detail': 'washers', 'amount': 31, 'term': datetime.date(2020, 2, 20), 'color': 'red',
                    'size': 20}])  # друга партія деталей
    p3 = np.array([{'detail': 'gears', 'amount': 56, 'term': datetime.date(2020, 1, 23), 'color': 'grey', 'size': 15},
                   {'detail': 'bolts', 'amount': 32, 'term': datetime.date(2020, 1, 22), 'color': 'black', 'size': 10},
                   {'detail': 'nuts', 'amount': 48, 'term': datetime.date(2020, 1, 19), 'color': 'white', 'size': 15},
                   {'detail': 'washers', 'amount': 79, 'term': datetime.date(2020, 1, 20), 'color': 'red',
                    'size': 20}])  # третя партія деталей
    while True:
        while flag == False:
            try:
                color = input(f'color of detail number: ')  # колір шуканої деталі
                size = int(input(f'size of detail number: '))  # розмір шуканої деталі
                break
            except ValueError:
                print('enter correct value')

        for i in p1:
            if i.get('color') == color and i.get('size') == size:  # перевіока та пошук деталі в партіях
                for j in p2:
                    if j.get('color') == color:
                        for k in p3:
                            if k.get('color') == color:
                                flag = True
                                amount = (i.get('amount')) + (j.get('amount')) + (
                                    k.get('amount'))  # підрахунок усіх детлей в різних партіях
                                print('total', i.get('detail'), ':', amount, )
                                if input('you want more information, press Enter ') == '':
                                    numb = int(input('number of party: '))  # номер партії для детальнішої інформації
                                    if numb == 1:
                                        print('retm: ', i.get('term'), ', amount on', numb, 'party:', i.get('amount'))
                                    elif numb == 2:
                                        print('retm: ', j.get('term'), ', amount on', numb, 'party:', j.get('amount'))
                                    elif numb == 3:
                                        print('retm: ', k.get('term'), ', amount on', numb, 'party:', k.get('amount'))
        if flag != True:
            print('you enter wrong color or size')
        else:
            break
    if input('if you want continue, press Enter ') != '':
        break
