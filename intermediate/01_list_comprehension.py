def multiply_by_three (number: int) -> int:
    return number * 3

fruits: list = ["Apple", "Grape", "Orange", "Watermelon"]
numbers: list = [2,4,3,1,5,6,7]
my_list: list = [i for i in fruits]
print(my_list)

# Puedes modificar los valores de una lista y pasarlos a otra en poco codigo esto da mas potencia
print(list(multiply_by_three(i) for i in numbers))