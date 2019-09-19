import random
def game():
      answer = input('Привет, хочешь сыграть в игру угадай число?')
      if answer == 'y':
          his = random.randint(0, 10)
          yours = int(input('Введи число от 1 до 10: '))
          if his == yours:
              print('Угадал! Сыграй еще раз.')
              game()
          else:
                  print('Не угадал, попробуй еще раз.')
                  game()
      else:
            print('Пока, возвращайся!')
            game()
game()
