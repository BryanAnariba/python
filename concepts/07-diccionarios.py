my_dict: dict = {}
my_other_dict: dict = dict()

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = { "name": "Goku", "surname": "Perez", "age": 30 }
print(my_other_dict)

my_dict = {
  "name": "Gohan",
  "surname": "Perez",
  "age": 18,
  "role": "Saiyan",
  "languages": {"Python", "NodeJS", "Typescript"}
}

print(my_dict)
print(my_dict["role"])

my_dict["role"] = "Hybrid Saiyan"

print(my_dict["role"])

del my_dict["role"]

print(my_dict)

print("surname" in my_dict)

print("Mas metodos")
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("name", 1, "floor"), None)) # Crea un diccionario nuevo pero sin valores {'name': None, 1: None, 'floor': None}