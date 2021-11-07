class Person:
    moods = ("Happy", "Lazy", "Tired")
    def __init__(self,name,money,mood,healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate
    def sleep(self, hours):
        self.mood = hours
        if self.mood == 7:
            print(Person.moods[0])
        elif self.mood < 7:
            print(Person.moods[1])
        elif self.mood > 7:
            print(Person.moods[2])

    def eat(self,meals):
        self.healthRate= meals
        if self.healthRate == 3:
            print("100% hth")
        elif self.healthRate == 2:
            print("75%")
        elif self.healthRate == 1:
            print("50%")




    def buy(self,items):
        self.money -= (items*10)
        print(self.money)
    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self,num):
        if num in range(0, 101):
          self.__healthRate = abs(num)
        else:
            print(" etween ")



p = Person("hamed",1000,7,2)
p.buy(1)
print(p)
p.sleep(4)
p.eat(p.healthRate)

