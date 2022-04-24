# ru_eng = {
#     'дверь': 'door',
#     'стол': 'table',
#     'стул': 'chair',
#     'ключ': ['key', 'fount', 'source', 'clue'],
# }

# <editor-fold desc="Обращение к словарю">

# print(ru_eng)
# print(ru_eng['дверь'])
# print(ru_eng['ключ'])

# </editor-fold>

# <editor-fold desc="Методы словаря">

# tmp = ru_eng.get('стол')
# ru_eng.pop('стол')
# print(ru_eng)
# tmp = ru_eng.copy()
# tmp = ru_eng.keys()
# tmp = ru_eng.values()
# print(ru_eng.items())

# for key in ru_eng.keys():
#     print(key, ":", ru_eng[key])

# </editor-fold>


users = {
    'e.azimov': 'Elvin123',
    'bot gabe': 'qwerty',
    'bot will': 'asdfg'
}

print(users)
users['e.azimov'] = 'Azimov123'
users['bot steve'] = 'Steve777'

tmp = users['bot steve']
users['bot steve'] = [tmp, 'New Steve111']
print(users)