# While
my_condition: int = 0
counter: int = 0
while my_condition < 10:
  print(my_condition)
  my_condition += 1

while counter < 20:
  counter += 1
  if (counter == 15):
    print(f"Counter value is {counter}, stopping loop")
    break
  print("Counter is minor than ", 20)

print("Exit While!!!")

# For
my_list = [1,2,4,5,6,7,8,8]

for element in my_list:
  print(element)

my_dict: dict = {"name": "goku", "surname": "perez", "age": 29, 1: "ups"}

for element in my_dict:
  print(element)
  if (element == "age"):
    break #continue
print("Exit For!!!")