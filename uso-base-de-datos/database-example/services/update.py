import pyodbc

def actualizar():
    try:
        # Conectamos por ahorita quiero que sea a SQL SERVER ya que este lo uso en el trabajo pero probare con MongoDB Despues
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=ANARIBA\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        conexion.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        cursor = conexion.cursor()

        stmt = 'UPDATE Persona SET nombrePersona = ?, apellidoPersona = ?, emailPersona = ? WHERE idPersona = ?'
        cursor.execute(stmt, [ 'Nombre Seis Modificado', 'Apellido Seis Modificado', 'testEmail6@gmail.com', 6 ]) # se puede actualizar con executemany varios pero para eso mejor ver el video completo, no lo considero necesario de momento

        cursor.commit()
        print(f'Registros Actualizados: { cursor.rowcount }')

    except Exception as ex:
        print(f'Ha Ocurrido un error: { ex }')
    finally:
        conexion.close()