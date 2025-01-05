def hello() -> None:
    print("Helloo!")

def my_function() -> str:
    return "This is a function"

def add_two_values(number_one: int, number_two: int) -> int:
    return number_one + number_two;

def get_values_with_default_value(name: str, surname: str, status: str = "Active"):
    return f'Name={name}, Surname={surname}, Status={status}'

def print_text(text: str) -> None:
    print(text)

hello()
print("function =", my_function())
print("1 + 2 =", add_two_values(1,2))
print(get_values_with_default_value("Gohan", "Perez"))