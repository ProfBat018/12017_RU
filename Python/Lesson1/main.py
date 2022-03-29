
# print("'Something in the way'")
# print('"Something in the way"')

# <editor-fold desc="Escape Sequences & Print">

# print("Hello", "World")     # Print - function, which takes endless arguments

# print("Hello")
# print("World")

# print("Hello", "\n", "World")
# print("Hello\nWorld")

# print("Hello\tWorld")
# print("Hello\new World")
# print("hello \\\\\\ World")
# print("\"Hello\"")
# print('\'Hello\'')

# </editor-fold>

# <editor-fold desc="Data Types">

# a = 5
# print(type(a))
# a = '5'
# print(type(a))
# a = True
# print(type(a))
# a = 3.25
# print(type(a))

# </editor-fold>

# <editor-fold desc="Naming Cases">

# FirstNumber = 10    # Pascal Case, также расценивается как upper camel case
# firstNumber = 10    # Camel Case - lower camel case
# first_number = 10   # Snake Case
# first-number = 10   # Kebab Case, нельзя ииспользовать в пайтон


# </editor-fold>

# <editor-fold desc="Input and Type Casting">


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

result = first_number + second_number

print(first_number, "+", second_number, "=", result)

print("{} + {} = {}" .format(first_number, second_number, result))

print(f"{first_number} + {second_number} = {result}")   # string interpolation


# </editor-fold>
