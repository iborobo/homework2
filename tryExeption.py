# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def minus(self,a,b):
#         return a-b
#     def mult(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
#     def proc(self,a,b):
#         return a%b
#     @staticmethod
#     def money():
#         print('babki goni:')
    
# cal=Calculator()

# class B(Calculator):
#     pass

# g = B()

# def Input():
#     x=int(input("first number: "))
#     y=int(input("second number: "))
#     return x,y

# znak=input("viberite(+,-,*,/,%)")

# if znak in ["+","-","*","/","%"]:
#     num1,num2=Input()

#     if znak=="+":
#         print("result: ",g.add(num1,num2) ,'гони бабки 100$')
#     if znak == '-':
#         print("result: ",g.minus(num1,num2), 'гони бабки 100$')
#     if znak == '*':
#         print("result: ",g.mult(num1,num2), 'гони бабки 100$')
#     if  znak == '/':
#         print("result: ",g.div(num1,num2), 'гони бабки 100$')
#     if znak == '%':
#         print('result:', g.proc(num1),'гони бабки 100$')

# class Bus:
#     def __init__(self,max_speed,mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# car = Bus(220,10000)
# print(car.max_speed,car.mileage)


# class Bus:
#     def __init__(self,name,speed,mileage):
#         self.name = name
#         self.speed = speed
#         self.mileage = mileage

# class Vehicle(Bus):
#     pass
# a = Vehicle('School Volvo',180,2000,'white')
# print('Vehicle NAme:',a.name,'Speed:', a.speed ,'Mileage:' ,a.mileage,)


# class First:
#     color = 'white'
#     def __init__(self,name,speed,mileage):
#         self.name = name
#         self.speed = speed
#         self.mileage = mileage

# class Second(First):
#     pass
# class Third(First):
#     pass

# a = Second('ai',120,2000)
# print(a.name,a.color,a.speed,a.mileage)

#23.05.2024
#classwork -> CRUD -> C -> Creat +
#                     R -> Read -
#                     U -> Update +
#                     D -> Delet +

# class Crud:
#     def __init__(self):
#         self.properties = {}


    # def update_property(self,property_id,new):
    #      self.properties[property_id] = new

#     def create_property(self,property_id,details):
#         self.properties[property_id] = details

#     def read_property(self,property_id):
#         return self.properties.get(property_id)
    
#     def update_property(self,property_id,new_details):
#         return self.properties[property_id] == new_details

#     def delete_property(self,property_id):
#         del self.properties[property_id]
# pro_sys = Crud()

# pro_sys.create_property(1,{"address":"123 Qora qmish 2/3"})
# print(pro_sys.read_property(1))
# pro_sys.update_property(2,{"address":"Shoyhon tumani"})
# print(pro_sys.read_property(2))
# pro_sys.delete_property(1)

# class Car1:
#     def __init__(self,marka,model,data_relise,price):
#         self.marka = marka
#         self.model = model
#         self.data_relise = data_relise
#         self.price = price
#     def results(self):
#         print(f"MArka:{self.marka} |",
#               f"Model: {self.model}|",
#               f"Data_relise: {self.data_relise}|",
#               f"Price: {self.price}"
#               )
         
# class Car2(Car1): 
#     pass        
# car = Car1("Chevrolet => Legkiy car","Matiz",2010,"5000$")

# car2 = Car2("Crans => trucks","Ford",2023,"15000$")

# car.results()
# car2.results()

# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self._species = None  
#         self.sound = sound
  
#     def set_species(self, species):
#         self._species = species

#     def get_species(self):
#         return self._species

#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name

#     def set_sound(self, sound):
#         self.sound = sound

#     def get_sound(self):
#         return self.sound
  
#     def display_info(self):
#         print(f"Species: {self.get_species()} | Name: {self.get_name()} | Sound: {self.get_sound()}")

# animal = Animal("cat", "myau")
# animal.set_species("sfinks")
# animal.display_info()

# def lol(s):
#     s = s.replace(" "," ")
#     return s == s[::-1]
# word = 
# if lol(word):
#     print(f"slova '{word}' yavlayetsa palindromom")
# else:
#     print(f"slova '{word}' ne yevlayetsa palindromom")
# print(word[::-1])

def vopros():
    a = "привет как дела"
    print
    c = input('я буду задавать тебе вопросы ты должен будешь отвечать ок?(+(да),-(нет)): ')
    if c == '+':
        print('well,lets start')
    elif c == '-':
        print('are u shure about that?!') 
    d = input('является ли слово "lox" полиндромом?(+(да),-(нет)): ')
    if d == '+':
        print('нет ты ошибся :(')
    elif d == '-':
        print('ну ты маладец :) ')
    e = input('является ли слово "saippuakivikauppias" полиндромом?(+(да),-(нет)):')
    if e == '+':
        print('хорош :)')
    elif e == '-':
        print('ну не повезло :(')
    f = input('является ли число "432" полиндромом?(+(да),-(нет)):')
 
    if f == '+':
        print('хорош :)')
    elif f == '-':
        print('ну не повезло :(')
    if d == '-' and e == '+' and f == '+':
        print('u tebya 3/3 pravelnih')
    elif d == '+' and e == '+' and f == '+':
        print('u tebya 2/3 pravelnih')
    elif  d == '-' and e == '-' and f == '+':
        print('u tebya 2/3 pravelnih')
    elif  d == '-' and e == '+' and f == '-':
        print('u tebya 2/3 pravelnih')
    elif  d == '+' and e == '-' and f == '+':
        print('u tebya 1/3 pravelnih')
    elif  d == '+' and e == '+' and f == '-':
        print('u tebya 1/3 pravelnih')
    elif d == '-' and e == '-' and f == '-':
        print('u tebya 1/3 pravelnih')
    elif d == '+' and e == '-' and f == '-':
        print('u tebya 0/3 pravelnih')
vopros()
