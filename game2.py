import random
attempts = 1
his = random.randint(1,10)
print ("Загадано число от 1 до 10")
yours = int(input("Ваш вариант? - "))
while his != yours:
    if his > yours: print ("Угадываемое число больше {0} ".format(his))
    elif his < yours: print ("Угадываемое число меньше {0} ".format(his))
    attempts += 1
    yours = int(input("Ваш вариант? - "))
print ("Вы угадали число {0} ".format(his))
print ("Вам потребовалось {0} попыток. ".format(attempts))
