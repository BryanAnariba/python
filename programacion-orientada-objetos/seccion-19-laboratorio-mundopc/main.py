from classes.Raton import Raton
from classes.Teclado import Teclado
from classes.Monitor import Monitor
from classes.Computadora import Computadora
from classes.Orden import Orden

def main():
    computadorasList: list =[]
    teclado = Teclado( 'Lenovo', 'Bluetooth' )
    monitor = Monitor( 'Huawei', 27 )
    raton = Raton( 'Logitec', 'USB' )
    computadoraGamer = Computadora( ' Gamer ', monitor, teclado, raton )
    
    teclado2 = Teclado( 'DELL', 'USER' )
    monitor2 = Monitor( 'DELL', 21 )
    raton2 = Raton( 'DELL', 'USB' )
    computadoraEmpresarial = Computadora( ' Desktop ', monitor2, teclado2, raton2 )

    teclado3 = Teclado( 'HP', 'USER' )
    monitor3 = Monitor( 'HP', 24 )
    raton3 = Raton( 'HP', 'USB' )
    computadoraEmpresarial2 = Computadora( ' HP ', monitor3, teclado3, raton3 )

    computadorasList.append( computadoraGamer )
    computadorasList.append( computadoraEmpresarial )

    # Orden
    orden1 = Orden( computadorasList )
    print(orden1)

    computadorasList.clear()
    computadorasList.append( computadoraEmpresarial2 )
    orden2 = Orden( computadorasList )
    print(orden2)
main()
