my_tuple: tuple = ()
my_other_tuple: tuple = ("Goku", "Saiyan", "Planeta Tierra", 1.80)

print(my_tuple)
print(my_other_tuple)
print(my_other_tuple[3])
print(my_other_tuple[1:3])
print(my_other_tuple.count("Goku"))
print(my_other_tuple.index("Planeta Tierra"))

# En las tuplas estos no se puede hacer ya que son inmutables, las listas si
# my_other_tuple[1] = "Super Saiyan"
# print(my_other_tuple)