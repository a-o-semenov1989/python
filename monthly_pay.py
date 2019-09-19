def bank():
    print('Здравствуйте, Вас приветствует Virtual Bank')
    income = int(input('Пожалуйста, укажите свой eжeмесячный доход: '))
    percent = int(input('Введите процент от ежемесячного дохода: '))
    summ = int(input('Введите сумму кредита: '))
    monthly_pay = income  / 100 * percent
    term = summ / monthly_pay
    print(' Ежемесячный платеж составляет ' + str(monthly_pay))
    print(' Вы погасите кредит за ' + str(term) + ' месяцев.')

balance = 10000
income = 20000
if income < 10000:
    print('Ваш ежемесячный доход не достаточен для обслуживания текущего кредита')

if balance >= 0:
    print('У вас положительный баланс на счету')

if income > 15000:
    print('Ваш доход позволяет вам взять выбранный кредит')

if income == 0:
    print('У вас нулевой доход')

if income and balance <= 0:
    print('У вас отрицательный доход и баланс на счету')

if income >= 0:
    print('У вас присутствует доход')


