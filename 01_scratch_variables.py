# comment
# there are no multiple lines comments

print("€: There is no need to specify the type of a variable")

x = 1
print(x)

print("€: How we know the type then?")

print(type(x)) # <class 'int'>

pi = 3.14159
print(type(pi)) # <class 'float'>

name = "Anya"
print(type(name)) # <class 'str'>


possible_number = "12" # 12
print(possible_number)
print(type(possible_number))
number = int(possible_number)
print(number)  # 12
print(type(number))


print("€: Python is dynamically typed")

possible_number = 12
print(type(possible_number)) # int

possible_number = "23"
print(type(possible_number)) # str


possible_number2 = "12a"
print(int(possible_number2))  # ValueError: invalid literal for int() with base 10: '12a'



