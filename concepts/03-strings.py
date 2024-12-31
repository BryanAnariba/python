my_string: str = 'My String\n'
my_other_string: str = 'My other String'
my_new_line_string: str = 'Hello \nWorld'
my_tab_string: str = 'Hello \tWorld'
first_name: str = 'Goku'
last_name: str = 'Perez'
age: int = 30

# 3:02

print(len(my_string))
print(len(my_other_string))
print(f'Cuantas n tiene: {my_string.count('n')}')
print(my_string + ' ' + my_other_string)
print(my_new_line_string)
print(my_tab_string)

print("My name is {} {} and my age is {}".format(first_name, last_name, age))
print("My name is %s %s and my age is %d"%(first_name, last_name, age))
print(f"My name is {first_name} {last_name} and my age is {age}")

# Partir strings, muy util
my_string_slice: str = my_string[1:4]
print(my_string_slice)
my_string_slice: str = my_string[-2]
print(my_string_slice)

# String al reves
my_string_reversed: str = my_string[::-1]
print("Cadena al reves: " + my_string_reversed)

print(f"python empieza con py: {"python".startswith("py")}")