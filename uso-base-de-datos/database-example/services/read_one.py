import pyodbc

def readOne():
    try:
        # Conectamos por ahorita quiero que sea a SQL SERVER ya que este lo uso en el trabajo pero probare con MongoDB Despues
        #conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=ANARIBA\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-S2CFA8N\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        conexion.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        conexion.autocommit = False
        cursor = conexion.cursor()

        # -------------------------------------------------------------- GET ONE -----------------------------------------------------
        print('\n#################################################################### GET ONE ###########################################################################################')
        stmt = 'SELECT  idPersona, nombrePersona, apellidoPersona, emailPersona FROM Persona WHERE idPersona = ?'
        cursor.execute(stmt, [4])
        row = cursor.fetchone()
        print(row)

    except Exception as ex:
        conexion.rollback()
        print(f'Ha Ocurrido un error: { ex }')
    finally:
        conexion.close()