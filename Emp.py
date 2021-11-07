from main import Person
import  re
class Employee(Person):
    def __init__(self,name ,money,mood,healthRate,id ,car ,email,salary,distanceToWork):
        super().__init__(name,money,mood,healthRate)
        self.id = id
        self.car = car
        self.__email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
    def work(self,hours):
        self.distanceToWork = hours
        if self.distanceToWork == 8:
            print(Person.moods[0])
        elif self.distanceToWork < 8:
            print(Person.moods[1])
        elif self.distanceToWork > 8:
            print(Person.moods[2])

    def drive(self):
        pass
    def refuel(self):
        pass
    def send_mail(self,to, subject, msg, receiver_name):
        self.to = to
        self.subject = subject
        self.msg = msg
        self.receiver_name = receiver_name
        file = f"to: {self.to} \n subject: {self.subject}  \n msg: {self.msg} \n receiver_name: {self.receiver_name}"
        filename = open("filename.txt" , "a")
        filename.write(file)
        filename.close()

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
         if salary < 1000:
             self.__salary = 1000
             print("df")
         else:
             self.__salary = abs(salary)
        ##self.__salary = sal
        #if self.__salary < 1000:
            #print("salary min 1000 plz")
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, mail):
        # if mail == "h":
        #     self.__email = mail
        # else:
        #     print("ff")
        reg =r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if re.match(reg, mail):
           self.__email = mail
        else:
             print("error")




em = Employee("hamed",100,7,3,25,2,"mohamedhame",100,7)
em.work(9)
em.send_mail("mohamedhamed@gmail.com","iti","how are you","hamed")
p =em.salary
print(em.email)