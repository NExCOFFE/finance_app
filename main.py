
from files.finance_app.client import *
from files.finance_app.plot import *
import os

if __name__ == '__main__':
    load()
    command = ''
    while command != '10':
        os.system('cls')
        print('Доступные действия ')
        print('1- посмотреть предложения о банке ')
        print('2- отправить жалобу ')
        print('3- информация о сщетах ')
        print('4- посмотреть прогноз доходов и расходов на следующий месяц ')
        print('5- добавить транзакцию ')
        print('6- посмотреть график доллара к рублю ')
        print('7- посмотреть график доллара к биткоину ')
        print('10- выйти')
        command = input('Выберите действия ')
        if command == '1':
            suggestions()
        elif command == '2':
            complains()
        elif command == '3':
            show_info()
        elif command == '4':
            predict()
        elif command == '5':
            make_trancastions()
        elif command == '6':
            plot_rub_usd()
        elif command == '7':
            plot_usd_btc()
        elif command == '10':
            print('Сохранение изменений ')
            save()
            print('Вы вошли')
        else:
            print('Вы не вошли')

        input()