name = "Elvin"

# w - write, wb - write bytes
# r - read, rb - read bytes
# a - append, ab - append bytes

# <editor-fold desc=Example 1>

# file = open("data.txt", 'a')
# file.write("\n" + name)
# file.close()

# </editor-fold>

# <editor-fold desc=Example 2>

# file = open("data.txt", 'w')
#
# cars = ['BMW', 'Mercedes', 'Audi']
#
# names = """Привет.
# Меня зовут
#             Эльвин        """
#
# file.writelines(names)
# file.close()

# </editor-fold>

# <editor-fold desc=Example 3>

file = open("data.txt", "r")

result = file.read()
print(result)

# result = file.readline()
# print(result)

# print(file.readline())
# print(file.readline())
# print(file.readline())


# result = file.readlines()
# print(result[1])
# print(result)

# </editor-fold>



