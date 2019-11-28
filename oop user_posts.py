class User():
      name = ''
      email= ''
      password= ''
      posts = []
      ban = False

      def showInfo(self):
          print('_____')
          print(self.name)
          print(self.email)
          print(self.password)

      def addPost(self):
            if self.ban == True:
                  print('Ты находишься в бане, не можешь добавлять посты')
            else:
                  text = input('Введи текст')
                  post = Post(text, self)
                  self.posts.append(post)

      def showPosts(self):
            print('Все посты юзера')
            for post in self.posts:
                  print(post.text)
                  print(post.userName)            

      def __init__(self, name, email, password):
          self.name = name
          self.email = email
          self.password = password
          self.posts = []
          print('Создан новый объект', self.name)

class Post():
      text = ''
      userName = ''

      def __init__(self, text, user):
            self.text = text
            self.userName = user.name

class SuperUser(User):
      def banUser(self, user):
            user.posts = []
            user.ban = True
            print('Я удалил все твои посты и отправил тебя в бан')

      def showInfo(self):
            print(self.name)
            print(self.email)
            print('Я злой админ')

admin = SuperUser('Daniil', 'daniil@mail.ru', 'qwerty')
admin.ShowInfo()

anatolii = User('Anatolii', 'anatolii@gmail.com', '12345')
anatolii.showInfo()

anatolii.addPost()
anatolii.addPost()
anatolii.addPost()
anatolii.showPosts()

boris = User('Boris', 'boris@gmail.com', 'ttt')
boris.showInfo()

anna = User('Anna', 'anna@gmail.com', 'qwerty')
anna.showInfo()
