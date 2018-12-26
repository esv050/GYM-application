import json
import os

date = input('Дата: ')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def begin():
    print('Меню\n'
          '1. Жим штанги лежа\n'
          '2. Приседание со штангой\n'
          '0. Вернуться в главное меню\n')
    choice = str(input('Выберите действие: '))
    if choice != '0':
        if choice == '1':
            choice = 'do1_'
            cls()
        if choice == '2':
            choice = 'do2_'
            cls()

        print('Меню\n'
              '1. Приступить к упражнению\n'
              '0. Вернуться назад\n')
        choice1 = int(input('Выберите действие: '))
        if choice1 != 0:
            cls()
            arr = []
            x = 0
            while x >= 0:
                weight = input('Подход № ' + str(x + 1) + ' вес: ')
                iteration = input('Подход № ' + str(x + 1) + ' повторы: ')
                arr.append(x + 1)
                arr.append(weight)
                arr.append(iteration)
                with open(choice + date, 'w') as file:
                    json.dump(arr, file)
                x += 1
                press = int(input('Меню\n'
                                  '1. Дополнительный подход\n'
                                  '0. Закончить упражнение\n'
                                  'Выберите действие: '))
                if press == 0:
                    break
            cls()
            begin()
        begin()


def statistic():
    choice2 = input('Меню\n'
                    '1. Жим штанги лежа\n'
                    '2. Приседание со штангой\n'
                    '0. Вернуться назад\n')
    if choice2 != '0':
        if choice2 == '1':
            choice2 = 'do1_'
        if choice2 == '2':
            choice2 = 'do2_'
        date1 = str(input('Дата тренировки: '))
        stats = open(choice2 + date1)
        stats_load = json.load(stats)
        for i in range(0, len(stats_load), 3):
            print('Подход: ' + str(stats_load[i]),
                  '\nВес: ' + stats_load[i + 1],
                  '\nКол-во повторений: ' + stats_load[i + 2], '\n')


menu = ''
while menu != 0:
    print('Главное меню\n'
          '1. Начать\n'
          '2. Статистика\n'
          '0. Выход\n')
    menu = int(input('Выберете действие: '))
    if menu == 1:
        cls()
        begin()
    if menu == 2:
        cls()
        statistic()
