from conexion import Conexion
from models.Persona import Persona

def getAll():
    cursor = Conexion().obtenerCursor()
    cursor.execute( 'SELECT * FROM Persona ORDER BY idPersona' )
    registros = cursor.fetchall()
    personas: list = []
    for registro in registros:
        persona = Persona( registro[0], registro[1], registro[2], registro[3] )
        personas.append( persona )

    #cursor.close()
    return personas

def getOne(idPersona: int):
    cursor = Conexion().obtenerCursor()
    cursor.execute('SELECT * FROM Persona WHERE idPersona = ?', [idPersona])
    registro = cursor.fetchone()
    persona = Persona( registro[0], registro[1], registro[2], registro[3] )
    cursor.close()
    return persona

def create():
    pass

def updateOne():
    pass

def deleteOne():
    pass

#print( getAll() )