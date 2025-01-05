# In python the way to create variables are with snake_case.

my_variable: str =' My string variable '
first_name: str = 'Goku'
last_name: str = 'Perez'
age: int = 30
is_active: bool = True
print(f'Type: {type(my_variable)} - Value: {my_variable}')
print(f'''
  USER INFO
  Complete name = {first_name.lower()} {last_name.upper()}
  Age = {age}
  Active = {'S' if is_active else 'N'}
  my_variable length: {len(my_variable)}
''')

employee_name: str = input('Write your name: ')
employee_age: int = int(input('Write your age: '))
print(f'Data: name={employee_name}, age={employee_age}')
