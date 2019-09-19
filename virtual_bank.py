bankInfo = {'version': 1.0, 'author': 'Anatolii Semenov'}
import os
import re
if not os.path.isdir('VirtualBank'):
    os.makedirs('VirtualBank')
os.chdir('VirtualBank')
def enterBank():
    print('Здравствуйте, Вас приветствует Virtual Bank')
    print('Версия банка', bankInfo['version'])
    print('Автор программы ' + bankInfo['author'])
    answer = input('Вы можете войти (1) или зарегистрироваться (2) ')
    if answer == '1':
        login()
    if answer == '2':
        registration()

def registration():
    name = input('Введите свое имя ')
    email = input('Введите адрес электронной почты ')
    password = input('Введите свой пароль ')
    if not os.path.isdir(email):
        os.makedirs(email)
        os.chdir(email)
        user_info = open('user_info.txt', 'w')
        user_info.write(name + '\n')
        user_info.write(email + '\n')
        user_info.write(password)
        user_info.close()
        print('Вы успешно зарегистрировались')
        credit()
    else:
        print('Пользователь с указанным email уже существует')
        registration()

def login():
    email = input('Введите адрес электронной почты ')
    password_login = input('Введите свой пароль ')
    if os.path.isdir(email):
        os.chdir(email)
        password = open('user_info.txt', 'r').readlines()[2]
        if password == password_login:
                print('Добро пожаловать')
                credit()
        else:
                print('Неверный пароль')
                login()
    else:
        print('Пользователь не найден, зарегистрируйтесь')
        registration()
        
def credit():
    answer = input('Вы можете выбрать потребительский кредит (1) или кредит для бизнеса (2), кредитную историю (3) и информацию по криптовалютам (4) ')
    if answer == '1':
        personal()
    if answer == '2':
        business()
    if answer == '3':
        credit_history()
    if answer == '4':
        cripto()

def personal():
    print('Потребительский кредит выдается суммой до 300000 на срок до 5 лет, процентная ставка составляет 10%')
    credit_summ = int(input('Укажите желаемую сумму кредита: '))
    credit_term = int(input('Укажите срок кредита: '))
    percent = 10
    if credit_summ > 30000 and credit_term > 5:
        print('Указано недопустимое значение')
        personal()
    else:
        monthly_pay = ((credit_summ * ( 1 + ((percent * credit_term) / 100))) / (12 * credit_term))
        print('Ваш ежемесячный платеж составляет: ' + str(monthly_pay))
        answer = input('Вы согласны с условиями кредитования? (1 - да, 2 - нет) ')
        if answer == '1':
            audit_personal(credit_summ, credit_term, monthly_pay)
            return credit_summ, credit_term, monthly_pay
        if answer == '2':
            enterBank()
             
def business():
    print('Кредит для бизнеса выдается суммой до 10000000 на срок до 25 лет, процентная ставка составляет 10%')
    credit_summ = int(input('Укажите желаемую сумму кредита: '))
    credit_term = int(input('Укажите срок кредита: '))
    percent = 10
    if credit_summ > 10000000 and credit_term > 25:
        print('Указано недопустимое значение')
        business()
    else:
        monthly_pay = ((credit_summ * ( 1 + ((percent * credit_term) / 100))) / (12 * credit_term))
        print('Ваш ежемесячный платеж составляет: ' + str(monthly_pay))
        answer = input('Вы согласны с условиями кредитования? (1 - да, 2 - нет)')
        if answer == '1':
            audit_business()
        if answer == '2':
            enterBank()    
    
def credit_history():
    if os.path.isfile('credit.txt'):
        print('Ваша кредитная история: ')
        credit_info_summ = open('credit.txt', 'r').readlines()[0]
        credit_info_term = open('credit.txt', 'r').readlines()[1]
        credit_info_monthly_pay = open('credit.txt', 'r').readlines()[2]
        print('Суммa кредита: ' + str(credit_info_summ))
        print('Срок кредита: ' + str(credit_info_term))
        print('Ваш ежемесячный платеж составляет: ' + str(credit_info_monthly_pay))
    else:
        print('У вас отсутствует кредитная история')
    
def cripto():
    print('Информация по криптовалютам: ')

def audit_personal(credit_summ, credit_term, monthly_pay):
    income = int(input('Пожалуйста, укажите свой eжeмесячный доход: '))
    experience = int(input('Введите свой стаж(в годах): '))
    if income >= 10000 and experience >= 1:
        print('Ваш доход и стаж роботы позволяют вам взять кредит ')
        credit_info = open('credit.txt', 'w')
        credit_info.write(str(credit_summ) + '\n')
        credit_info.write(str(credit_term) + '\n')
        credit_info.write(str(monthly_pay))
        credit_info.close()
    else:
        print('Ваш доход и стаж роботы не позволяют вам взять кредит')
        enterBank()
    
def audit_business(credit_summ, credit_term, monthly_pay):
    income = int(input('Пожалуйста, укажите eжeмесячный доход своего бизнеса: '))
    experience = int(input('Введите свой срок действия своего бищнеса(в годах): '))
    if income >= 30000 and experience >= 1:
        print('Доход вашего бизнеса и срок его действия позволяют вам взять кредит ')
        credit_info = open('credit.txt', 'w')
        credit_info.write(str(credit_summ) + '\n')
        credit_info.write(str(credit_term) + '\n')
        credit_info.write(str(monthly_pay))
        credit_info.close()
    else:
        print('Доход вашего бизнеса и срок его действия не позволяют вам взять кредит')
        enterBank()
