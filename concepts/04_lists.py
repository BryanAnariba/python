my_list: list = []
my_other_list: list = list()

print(f'my_list: {len(my_list)}')

my_list = [18, 19, 20, 21, 22, 23]
my_other_list = [35, 1.77, "Gohan", "Gohan"]
print(my_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list.count("Gohan")) # 2 Registros

# Operaciones con listas
## Create
my_list.append("New naram")
my_list.insert(1, "Other new param")
print('======= Operations with lists =======')

## Delete y Delete Last Param, tambien el pop podes mandarle el indice del parametro a eliminar
my_list.remove(18) # Eliminamos la primer ocurreancia del 18
print(my_list.pop()) # Eliminamos el ultimo

print(my_list)

## Clear
my_other_list.clear()
print(f'my_other_list {my_other_list}')

my_other_list = my_list.copy()
print(f'my_other_list {my_other_list}')

numbers_list = [1,2,6,4,5]
print("Normal numbers_list: ", numbers_list)
numbers_list.reverse()
print("Reversed numbers_list: ", numbers_list)

# Ordenamiento
numbers_list.sort()
print("Sorted List: ", numbers_list)

# Rebanamiento de listas o partidas de [x,y] rango
print("Slice: " , numbers_list[1:3])
