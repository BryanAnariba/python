class Person:
    def __init__(self, name: str, sur_name: str, alias: str = "Without alias") -> None:
        self.__name = name
        self.__sur_name = sur_name
        self.__alias = alias
    
    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name
    
    def set_sur_name(self, sur_name: str) -> None:
        self.__sur_name = sur_name

    def get_surname(self) -> str:
        return self.__sur_name

    def i_am_walking(self) -> str:
        return f'{self.__name} alias {self.__alias} is walking!!!'


my_person = Person("Goku", "Kakaroto")
print(f'my_person: {my_person.get_name()} {my_person.get_surname()}')
print(my_person.i_am_walking())