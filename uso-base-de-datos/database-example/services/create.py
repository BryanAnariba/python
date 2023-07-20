import pyodbc

def create():
    try:
        # Conectamos por ahorita quiero que sea a SQL SERVER ya que este lo uso en el trabajo pero probare con MongoDB Despues 
        #conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=ANARIBA\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-S2CFA8N\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        conexion.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        conexion.autocommit = False
        cursor = conexion.cursor()
        # -------------------------------------------------------------- CREATE -----------------------------------------------------
        stmt = 'SELECT dbo.getLastIdFromPersona() AS idPersona'
        row = cursor.execute(stmt)
        idPersona = row.fetchval()
        stmt = 'INSERT INTO Persona( idPersona, nombrePersona, apellidoPersona, emailPersona ) VALUES (?,?,?,?)'
        nombrePersona = 'Nombre Seis'
        apellidoPesona = 'Apellido Seis'
        emailPersona = 'test6@gmail.com'
        cursor.execute(stmt, [ idPersona, nombrePersona, apellidoPesona, emailPersona ]) # CON EXECUTEMANY insertas varios, pero debes mandar una tupla de tuplas o un array de objetos para acerlo masivo
        cursor.commit()
        print(f'Registros insertados: { cursor.rowcount }')
        cursor.close()
    except Exception as ex:
        conexion.rollback()
        print(f'Ha Ocurrido un error: { ex }')
    finally:
        conexion.close()