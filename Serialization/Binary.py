import pickle   # библиотека для бинарной сериализации

# <editor-fold desc="Write Bytes">

# users = {
#     'Elvinos018': 'Elvin123',
#     'Nightcal018': 'Nightcall'
# }
#
# file = open("data.txt", 'wb')
#
# pickle.dump(users, file)

# </editor-fold>

# <editor-fold desc="Read Bytes">

# file = open("data.txt", "rb")
#
# users = pickle.load(file)
# print(users)
# print(type(users))

# </editor-fold>

# <editor-fold desc="Serialize list">
# file = open("cars.txt", 'wb')
#
# cars = ["Mercedes", "Chevrolet", "Ford"]
#
# pickle.dump(cars, file)
#
# file.close()
# </editor-fold>

# <editor-fold desc="Deserialize list">

# file = open("cars.txt", 'rb')
#
# a = pickle.load(file)
#
# print(a)
#
# file.close()

# </editor-fold>


class Person:
    def __init__(self, _name, _surname, _age):
        self.name = _name
        self.surname = _surname
        self.age = _age

    def __str__(self):
        return f"Name is: {self.name}\n" \
               f"Surname is: {self.surname}\n" \
               f"Age is: {self.surname}\n"

    def say_hello(self):
        print(f"{self.name} says hello")


# p1 = Person("Elvin", "Azimov", 20)
# print(p1)
#
# p1.say_hello()
#
# file = open("person.txt", 'wb')
# pickle.dump(p1, file)
#
# file.close()


# file = open("person.txt", 'rb')
#
# p2: Person = pickle.load(file)
#
# print(p2)
#
# p2.say_hello()
#
# file.close()

import time

a = time.gmtime()

print(a.tm_year)
print(a.tm_mon)
print(a.tm_mday)
print(a.tm_hour)
print(a.tm_min)
print(a.tm_sec)

