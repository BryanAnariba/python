from classes.Bicicleta import Bicicleta
from classes.Coche import Coche

def main():
    nuevaBicicletaBacini = Bicicleta( 'Gris', 2, 'Carretera' )
    print( nuevaBicicletaBacini )

    hondaCivic = Coche( 'Beige', 5, 240 )
    print( hondaCivic )

main()