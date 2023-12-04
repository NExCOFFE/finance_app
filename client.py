
import json

client_info = {}

def load():
    global client_info
    with open('client_info.json', 'r', encoding='utf-8') as json_file:
        client_info = json.load(json_file)
def save():
    global client_info
    with open('client_info.json', 'w', encoding='utf-8') as outfile:
        json.dump(client_info, outfile)
def show_info():
    global client_info
    print("Информация о счетах")
    print("----------------------------------")
    for account in client_info['accounts']:
        print('Имя',account['name'])
        print('Платежная система',account['system'])
        print('Номер', account['number'])
        print('Баланс', account['balance'])
        print('Тип:', account['type'])
        print('Срок действия',account['validity period'])
        print("----------------------------------")
def predict():
    global client_info
    expenses = 0
    income = 0
    months = []
    for transaction in client_info['transactions']:
        if transaction['type'] == 'списание':
            expenses += transaction['amount']
        if transaction['type'] == 'зачисление':
            income += transaction['amount']

        if transaction['date'] not in months:
            months.append(transaction['date'])
    print('Предполагаемые расходы в следующем месяце:', expenses / len(months))
    print('Предполагаемые доходы в следующем месяце', income / len(months))
def suggestions():
    f = open('suggestions.txt', 'r', encoding='utf-8')
    text = f.read()
    print(text)
    f.close()
def complains():
    with open('complains.txt', 'a', encoding='utf-8') as f:
        user = input('Введите жалобу: ')
        f.write('\n' + user)
        print('Ваша жалоба будет расмотрена в скором времени ')

def make_trancastions():
    global client_info
    print('Доступные счета ')
    i = 1
    for account in client_info['accounts']:
        print(i ,'-', account['name'], '-', account['number'])
        i += 1

    try:
        account_num = int(input('Введите номер счета: '))
    except:
        print('Ошибка кода. Прерываю транзакцию')
        return
    for i in range(len(client_info['accounts'])):
        if i + 1 == account_num:
            account = client_info['accounts'][i]['number']
            break
    else:
        print('Такого номера не существует. Прерываю транзакцию')
        return

    
    print('Типы транзакций: ')
    print('1-списание')
    print('2-Зачисление')
    a = input('Выберите тип транзакции: ')
    if a == '1':
        a = 'списание'
    elif a == '2':
        a = 'зачисление'

    else:
        print('Такого типа не существует.Прерываю транзакцию')
        return

    print("Дата транзакции")
    year = input("Введите год: ")
    month = input("Введите месяц: ")

    if int(year) > 2023 or int(month) > 12 or int(month) < 1:
        print("Неверная дата прерываю транзакцию")
        return
    
   
    try:
        amount = int(input('Введите сумму: '))
    except:
        print('Ошибка ввода. Прерываю транзакцию ')
        return
    if amount < 1:
        print("Сумма не может быть меньше 1. Прерываю транзакцию")
        return
    

    if a  == "списание":
        client_info["accounts"][account_num-1]["balance"] -= amount
    elif a == "зачисление":
        client_info["accounts"][account_num-1]["balance"] += amount

    client_info["transactions"].append({"account": account,
                                        "type": a,
                                        "date": {"year": 2023, "month": 12},
                                        "amount": amount})

    print("Транзакция записана. Текущий баланс на счёте: ")
    print(client_info["accounts"][account_num-1]["balance"])
    new_data = {"account": account,
                "type": a,
                "date": {"year": 2023, "month": 12},
                "amount": amount}






# load()
# show_info()
# make_trancastions()
# complains()
# predict()
# suggestions()
#





