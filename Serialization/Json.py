# https://api.openweathermap.org/data/2.5/weather?q=Baku&appid=5191fee1957155f779bfd029a4a97e18

# import requests
#
# response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Baku&appid=5191fee1957155f779bfd029a4a97e18")
# result = response.text
import json


class Person:  # class user defined data type
    def __init__(self, _name: str = '', _surname: str = '', _age: int = 0):  # init - cosntructor
        self.name = _name
        self.surname = _surname
        self.age = _age

    def __str__(self):
        return f"{self.name}\n{self.surname}\n{self.age}\n"

    @staticmethod   # decorator
    def from_dict(data: dict):
        return Person(data["name"], data["surname"], data["age"])


# <editor-fold desc="Serialize Json">

# p1 = Person("Elvin", "Azimov", 20)
# p2 = Person("Ervin", "Aghakishi", 15)
#
# people = [p1, p2]
#
# data = json.dumps(people, default=lambda x: x.__dict__)
#
# file = open("data.json", 'w')
# file.write(data)

# </editor-fold>

# <editor-fold desc="DeSerialize Json">

file = open("data.json", 'r')

data = json.load(file)  # de serialization

a = Person.from_dict(data[0])

# </editor-fold>
