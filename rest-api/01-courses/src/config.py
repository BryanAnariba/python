from distutils.command.config import config


class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'coursedev'

config = {
    'development': DevelopmentConfig
}