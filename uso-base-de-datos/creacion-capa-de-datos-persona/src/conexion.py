import pyodbc
import sys
from logger_base import log

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'bryansanchez'
    _PASSWORD = 3500
    _HOST = 'DESKTOP-S2CFA8N\SQLEXPRESS'
    _conexionStr = 'DRIVER={SQL Server};SERVER=' + _HOST + ';DATABASE=' +  _DATABASE + ';UID=' + _USERNAME + f';PWD={  _PASSWORD }' 
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion == None:
            try:
                cls._conexion = pyodbc.connect(cls._conexionStr)
                cls._conexion.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
                cls._conexion.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
                #log.debug( f'Conexion exitosa: { cls._conexion }' )
                return cls._conexion
            except Exception as ex:
                log.error( f'Ha ocurrido una excepcion en la ejecucion de la conexion: { ex }' )
                sys.exit()
        else:
            return cls._conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor == None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                #log.debug( f'Se abrio correctamentre el cursor: { cls._cursor }' )
                return cls._cursor
            except Exception as ex:
                log.error( f'Ha ocurrido una excepcion en la ejecucion del cursor: { ex }' )
        else:
            return cls._cursor
        
# testConexion = Conexion()
# testConexion.obtenerConexion()
# testConexion.obtenerCursor()
                


