# No son estructuras ordenadas, es aleatorio o random, y no acepta duplicados
# 5: 00
my_set: set = set()
my_other_Set: set = {"Gohan", 14, "Hybrid Saiyan"}

print(type(my_set))
print(type(my_other_Set))
print(len(my_other_Set))

# No acepta duplicados los omite
my_other_Set.add("Niklaus")
my_other_Set.add("Niklaus")

print(my_other_Set)

# Verificar si un campo existe en un set
print("Niklaus" in my_other_Set)
print("klaus" in my_other_Set)

# Eliminar datos
my_other_Set.remove("Niklaus")
print(my_other_Set)

my_other_Set.clear()

print(my_other_Set)

# Casteo
my_set = {"Gohan", 14, "Hybrid Saiyan"}
my_list = list(my_set)
print(my_list)