import pyodbc

def readAll():
    try:
        # Conectamos por ahorita quiero que sea a SQL SERVER ya que este lo uso en el trabajo pero probare con MongoDB Despues
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=ANARIBA\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        conexion.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        cursor = conexion.cursor()

        # -------------------------------------------------------------- GET ALL -----------------------------------------------------
        print('\n#################################################################### GET ALL ###########################################################################################')
        # Creamos un cursor para hacer un statement
        stmt: str = 'SELECT idPersona, nombrePersona, apellidoPersona, emailPersona FROM Persona WHERE idPersona IN (?,?,?)'
        inValues = ((1,2,3))
        cursor.execute(stmt, inValues)
        rows = cursor.fetchall()
        print('IMPRIMIENDO TODO LO QUE RETORNA EL SQL: ', rows)
        # Uno a Uno
        # print('\nIMPRIMIENDO LINEA A LINEA, NO MUY UTIL PARA ENVIARLO AL FRONTEND PERO PARA ALGO SIRVE: ')
        # for row in rows:
        #     print(row)
        cursor.close()
    except Exception as ex:
        print(f'Ha Ocurrido un error: { ex }')
    finally:
        conexion.close()