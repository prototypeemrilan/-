# Наследование, полиморфизм
# инкапсуляция

class Robot:
    brain = True
    def __init__(self,name,model,color,destination):
        self.name = name
        self.model = model
        self.color = color
        self.destination = destination
    def __str__(self):
        return f'name is:{self.name}\n' \
               f'color is:{self.color}\n' \
               f'model is:{self.model}\n'
    def desti(self):
        print(self.destination)


robot=Robot('Вдал', "А4", 'blue', 'снимать видео')
print(robot, robot.desti())

#Супер класс, дочерный класс

class Robot2(Robot):
    brain = False
    def __init__(self, name, model, color, destination, fly):
        super().__init__(name, model, color, destination)
        Robot.__init__(self,name, model, color, destination)
        self.fly = fly
    def desti(self):
        self.fly=False
        print(self.fly)

robot2=Robot2('termonator', 'T1001', 'pink', 'отбирает одежду',True)
print(robot2.fly)
robot2.desti()
print(robot2.fly)
print(robot2.brain, robot.brain)

class Robot3(Robot2):
    def desti(self):
        print(self, 'теперь он летает')

Terminal=Robot3('Optima bank', 'виза', 'red', 'ты бедный на карте нет денег', False)
Terminal.desti()

class Human:
    head = 1
    body = 1
    hands = 2

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print(f'{self.name} is run')

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Возраст{self.age}\n' \
               f'Тело{self.head}\n'

hum=Human('Алдияр', 18)
Terminal.desti(hum.name)