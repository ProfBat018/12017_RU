# <editor-fold desc="Inheritance and Polymorphism">

# class Entity:
#     def __init__(self, _name, _age, _type):
#         self.name = _name
#         self.age = _age
#         self.type = _type
#
#
# class Human(Entity):
#     def __init__(self, _name, _age, _type, _surname):
#         super().__init__(_name, _age, _type)
#         self.surname = _surname
#
#     def eat(self):
#         print(f"{self.name} eats")
#
#     def sleep(self):
#         print(f"{self.name} sleeps")
#
#     def __str__(self):
#         return f"{self.name}\n" \
#                f"{self.age}\n" \
#                f"{self.type}\n" \
#                f"{self.surname}\n"
#
#
# class Cat(Entity):
#     def __init__(self, _name, _age, _type, _breed):
#         super().__init__(_name, _age, _type)
#         self.breed = _breed
#
#     def eat(self):
#         meal_name = input("enter meal name: ")
#         print("You have to pet cat, to ask it for eat")
#         print(f"{self.name} eats, {meal_name}")
#
#     def sleep(self):
#         print(f"{self.name} sleeps")
#
#     def __str__(self):
#         return f"Kotik is {self.name}"
#
#
# a = Human("Elvin", 20, "Human", "Azimov")
#
# print(str(a))

# </editor-fold>

# <editor-fold desc="Incapsulation">

class Date:
    def __init__(self, day: str, month: str, year: str):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


class Product:
    def __init__(self, name: str, price: float, count: int, expiration_date: Date):
        self.name = name
        self.price = price
        self.__count = count
        self.__expiration_date = expiration_date

    @property
    def count(self):    # getter count_get
        return self.__count

    @count.setter       # setter count_set
    def count(self, value):
        self.__count += value
        if self.__count > self.__count * 10 / 100:
            self.price -= 0.20

    def __str__(self):
        return f"{self.name}\n" \
               f"{self.price}\n" \
               f"{self.__count}\n" \
               f"{self.__expiration_date}\n"

# </editor-fold>


lays = Product("Lays MAX", 2.40, 268, Date("01", "01", "2023"))

print(lays.count, lays.price)
lays.count = 500
print(lays.count, lays.price)

# self.name public (абсолютно общедоступный)
# self._name protected (доступен только внутри класса и в классах наследниках)
# self.__name private (доступен только внутри класса)
