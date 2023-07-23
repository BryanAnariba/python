from persona_service import getAll, getOne

def main() -> None:
    # Obtenemos todos las personas
    databaseResponse = getAll()
    for data in databaseResponse:
        print(f'GET ALL: { data }')

    # Obtenemos una persona
    databaseResponse = getOne(3)
    print(f'GET ONE: { databaseResponse }')

    # Creamos una persona
main()