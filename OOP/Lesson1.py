# Object Oriented Programming

# <editor-fold desc="Part 1">

class Person:   # class user defined data type
    def __init__(self, _name: str, _surname: str, _age: int):     # init - cosntructor
        self.name = _name
        self.surname = _surname
        self.age = _age

    def print_person(self):
        print(f"{self.name}\n"
              f"{self.surname}\n"
              f"{self.age}\n")

#
# p1 = Person("Elvin", "Azimov", 20)
# p2 = Person("Ervin", "Aghakishi", 15)
# p3 = Person("Ruslan", "Qaflanov", 32)
# p4 = Person("Ulker", "Hasanova", 22)
# p5 = Person("Jamila", "Heydarova", 18)
# p6 = Person("Ahmad", "Eynullayev", 24)
#
# people = [p1, p2, p3, p4, p5, p6]
#
# for item in people:
#     item.print_person()

# </editor-fold>

# <editor-fold desc="Part 2">

# class Person:
#     def __init__(self, _name: str, _surname: str, _age: int):  # init - cosntructor
#         self.name = _name
#         self.surname = _surname
#         self.age = _age
#
#     def __str__(self):  # logic of automatic type cast to string
#         return f"{self.name}\n{self.surname}\n{self.age}\n"
#
#     def __ge__(self, other):    # overload operator >=
#         return self.age >= other.age
#
#     def __gt__(self, other):    # overload operator >
#         return self.age > other.age
#
#     def __le__(self, other):    # overload operator <=
#         return self.age <= other.age
#
#     def __lt__(self, other):    # overload operator <
#         return self.age < other.age
#
#     def __eq__(self, other):    # overload operator ==
#         return self.age == other.age
#
#     def change_name(self, new_name: str):
#         self.name = new_name
#
#
# p1 = Person("Elvin", "Azimov", 20)
# p2 = Person("Ervin", "Aghakishi", 15)
#
# p1.change_name("Samir")
# print(p1)


# </editor-fold>

