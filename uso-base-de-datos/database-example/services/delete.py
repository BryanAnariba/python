import pyodbc

def eliminar():
    try:
        # Conectamos por ahorita quiero que sea a SQL SERVER ya que este lo uso en el trabajo pero probare con MongoDB Despues
        #conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=ANARIBA\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-S2CFA8N\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        conexion.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        conexion.autocommit = False
        cursor = conexion.cursor()

        stmt = 'DELETE FROM Persona WHERE idPersona = ?' # TAMBIEN SE PUEDEN ELIMINAR VARIOS PERO EN MAYORIA DE OCACIONES PREFERIREMOS HACER UN SOFTDELETE
        cursor.execute(stmt, 7)
        cursor.commit()
        print(f'Registros Eliminados: { cursor.rowcount }')
    except Exception as ex:
        conexion.rollback()
        print(f'Ha Ocurrido un error: { ex }')
    finally:
        conexion.close()