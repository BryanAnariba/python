import logging as log

log.basicConfig( 
    level=log.DEBUG, format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s', 
    datefmt='%I:%M:%S %p', 
    handlers=[ 
        log.FileHandler('capa_datos.log'), 
        log.StreamHandler() 
    ] ,
)

'''
log.debug( 'Mensaeje a nivel de debug' )
log.info( 'Mensaje a nivel de info' )
log.warning( 'Mensaje a nivel de warning' )
log.error( 'Mensaje a nivel de error' )
log.critical( 'Mensaje a nivel critico' )
'''