posicionesRobotMarte = [
    [ 33.4, 45.66, '2022/12/12 11:18:00' ],
    [ 43.4, 55.66, '2022/12/12 11:18:10' ],
    [ 53.4, 65.66, '2022/12/12 11:18:20' ],
    [ 63.4, 75.66, '2022/12/12 11:18:30' ],
    [ 73.4, 85.66, '2022/12/12 11:18:40' ],
    [ 83.4, 95.66, '2022/12/12 11:18:50' ]
]

print( 
    "Columnas: ",
    "Latitud =", posicionesRobotMarte[0][0], 
    "Longitud =", posicionesRobotMarte[0][1],
    "FechaHoraPosicionamiento =", posicionesRobotMarte[0][2] 
)

# Recorido
for posicion in posicionesRobotMarte:
    print( posicion )