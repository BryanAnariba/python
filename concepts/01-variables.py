# In python the way to create variables are with snake_case.
# 1 Hora
my_variable: str ='My string variable'
first_name: str = 'Goku'
last_name: str = 'Perez'
age: int = 30
is_active: bool = True

print(f'Type: {type(my_variable)} - Value: {my_variable}')
print(f'''
  USER INFO
  Complete name = {first_name} {last_name}
  Age = {age}
  Active = {  'S' if is_active else 'N'}
''')