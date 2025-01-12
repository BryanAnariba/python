### Challenges ###

'''
    Escribe un programa que muestre por consola (print) los numeros del 1 al 100 (ambos incluidos
    con un salto de linea entre cada impresion), sustituyendo los siguientes
    - Multiplos de 3 por la palabra "fizz"
    - Multiplos de 5 por la palabra "buzz"
    - Multiplos de 3 y 5 por la palabra "fizzbuzz"
'''
def fizz_buzz(number: int) -> None:
    for i in range(number):
        if (((i+1) % 3) == 0 and  ((i+1) % 5) == 0):
            print(f'{(i+1)} fizzbuzz')
        elif (i+1) % 3 == 0:
            print(f'{(i+1)} fizz')
        elif ((i+1) % 5) == 0:
            print(f'{(i+1)} buzz')
        else:
            print(f'{i + 1} no es multiplo de 3 o 5')
fizz_buzz(100)

'''
    Escribe una funcion que reciba dos palabras (String) y retorne Verdadero o Falso, segun sea o no
    anagramas.
    - Un anagrama consiste en formar una palabra reordenando todas, las letras de otra palabra inicial
    - No hace faltaa comprobar que ambas palabras existan
    - Dos palabras exactamente iguales no son anagramas
'''
def is_anagram(string_param_one: str, string_param_two: str) -> bool:
    string_param_one_lower: str = string_param_one.lower()
    string_param_two_lower: str = string_param_two.lower()
    
    print(sorted(string_param_one_lower))
    print(sorted(string_param_two_lower))

    if string_param_two_lower == string_param_one_lower:
        return False
    else:
        return True

print(f'Is anagram: amoR ↔ romA: {is_anagram("amoR", "amoR")}')
print(f'Is anagram: amoR ↔ romA: {is_anagram("amoR", "romA")}')
print(f'Is anagram: Cielo ↔ Liceo : {is_anagram("Cielo", "Liceo")}')