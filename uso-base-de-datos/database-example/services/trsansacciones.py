import pyodbc as db

def create():
    try:
        # Conectamos por ahorita quiero que sea a SQL SERVER ya que este lo uso en el trabajo pero probare con MongoDB Despues 
        #conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=ANARIBA\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')
        conexion = db.connect('DRIVER={SQL Server};SERVER=DESKTOP-S2CFA8N\SQLEXPRESS;DATABASE=test_db;UID=bryansanchez;PWD=3500')

        # Deshabilitar el commit automatico ojo esto es recomendado y lo e oido que en el mundo real esto no esta activo
        conexion.autocommit = False

        conexion.setdecoding(db.SQL_CHAR, encoding='utf-8')
        conexion.setdecoding(db.SQL_WCHAR, encoding='utf-8')
        cursor = conexion.cursor()

        # -------------------------------------------------------------- CREATE -----------------------------------------------------
        stmt = 'SELECT dbo.getLastIdFromPersona() AS idPersona'
        row = cursor.execute(stmt)
        idPersona = row.fetchval()
        stmt = 'UPDATE Persona SET nombrePersona = ?, apellidoPersona = ? WHERE idPersona = ?'
        nombrePersona = 'Nombre 6 Modificado'

        #Simulamos un truncate para ver el rollback
        #apellidoPesona = 'Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado Apellido 6 Modificado'
        apellidoPesona = 'Apellido 6 Modificado'
        cursor.execute(stmt, [ nombrePersona, apellidoPesona, 6 ]) # CON EXECUTEMANY insertas varios, pero debes mandar una tupla de tuplas o un array de objetos para acerlo masivo
        cursor.commit()
        print(f'Registros insertados se commiteo: { cursor.rowcount }')
        cursor.close()
    except Exception as ex:
        conexion.rollback()
        print(f'Ha Ocurrido un error se hizo rollback: { ex }')
    finally:
        conexion.close()

create()
