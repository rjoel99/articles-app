'''
Author: Joel Rubio
Date: 22-06-2022
'''

from mysql.connector import connect, Error
from datetime import datetime
from logs import Log
from utils import from_config
from os import environ


'''
Clase que representa un registro
de la consulta sobre la tabla de
articulos y articulos_ropa_detalles
'''
class ArticleClothesDetail(object):
    def __init__(self, id_article, id_clothes, fk_id_article, type_clothes, usability, size, season, color):
        self.__id_article    = id_article
        self.__id_clothes    = id_clothes
        self.__fk_id_article = fk_id_article
        self.__type          = type_clothes
        self.__usability     = usability
        self.__size          = size
        self.__season        = season
        self.__color         = color

    def serialize(self):
        return {
            'id artículo': self.__id_article,
            'id prenda': self.__id_clothes,
            'fK id artículo': self.__fk_id_article,
            'tipo': self.__type,
            'usabilidad': self.__usability,
            'talla': self.__size,
            'temporada': self.__season,
            'color': self.__color
        }


'''
Clase que representa un registro
de la consulta sobre la tabla de
articulos y articulos_accesorios_detalles
'''
class ArticleAccessoryDetail(object):
    def __init__(self, id_article, id_accessory, fk_id_article, type_clothes, color):
        self.__id_article    = id_article
        self.__id_accesory   = id_accessory
        self.__fk_id_article = fk_id_article
        self.__type          = type_clothes
        self.__color         = color

    def serialize(self):
        return {
            'id artículo': self.__id_article,
            'id accesorio': self.__id_accesory,
            'fk id artículo': self.__fk_id_article,
            'tipo': self.__type,
            'color': self.__color
        }

'''
Clase que representa un registro
de la consulta sobre la tabla de
articulos y articulos_calzadoos_detalles
'''
class ArticleShoeDetail(object):
    def __init__(self, id_article, id_shoe, fk_id_article, type_clothes, usability, number, color):
        self.__id_article    = id_article
        self.__id_shoe       = id_shoe
        self.__fk_id_article = fk_id_article
        self.__type          = type_clothes
        self.__usability     = usability
        self.__number        = number
        self.__color         = color

    def serialize(self):
        return {
            'id artículo': self.__id_article,
            'id calzado': self.__id_shoe,
            'fk id artículo': self.__fk_id_article,
            'tipo': self.__type,
            'usabilidad': self.__usability,
            'número': self.__number,
            'color': self.__color
        }
'''
Clase que representa las operaciones
realizadas en una base de datos,
como consulta, inserción, modificación,
eliminación, etc.
'''
class ArticleRepository:
    def __init__(self):
        self.__article_log = ArticleLog()

    #__config   = from_config('config.ini')
    __host     = environ.get('MYSQL_HOST', '172.30.178.181')
    __username = environ.get('MYSQL_USERNAME')
    __password = environ.get('MYSQL_PASSWORD')
    __database = environ.get('MYSQL_DATABASE')
    
    __table_article                 = "articulos"
    __table_article_clothes_det     = "articulos_ropa_detalles"
    __table_article_accessories_det = "articulos_accesorios_detalles"
    __table_article_shoes_det       = "articulos_calzados_detalles"

    __SELECT_CLOTHES_QUERY = f'''
    
        SELECT {__table_article}.id, {__table_article_clothes_det}.*
        FROM {__table_article}
        JOIN {__table_article_clothes_det}
            ON {__table_article}.id = {__table_article_clothes_det}.idArticulo
    '''

    __SELECT_ACCESSORIES_QUERY = f''' 

        SELECT {__table_article}.id, {__table_article_accessories_det}.*
        FROM {__table_article}
        JOIN {__table_article_accessories_det}
            ON {__table_article}.id = {__table_article_accessories_det}.idArticulo
    '''

    __SELECT_SHOES_QUERY = f'''

        SELECT {__table_article}.id, {__table_article_shoes_det}.*
        FROM {__table_article}
        JOIN {__table_article_shoes_det}
            ON {__table_article}.id = {__table_article_shoes_det}.idArticulo
    '''

    __CREATE_TABLE = f''' create table if not exists clientes(
            id int auto_increment primary key,
            nombre varchar(20) not null,
            apellido varchar(20) not null,
            edad int,
            direccion varchar(50),
            email varchar(40),
            telefono varchar(25),
            tipoDocumento enum('DNI','LIBRETA_CIVICA','LIBRETA_ENROLAMIENTO','PASAPORTE'),
            numeroDocumento varchar(10)
        );
    '''


    def find_articles_by_clothes_category(self):
        '''
        Obtiene los artículos por categoría de ropa
        de la base de datos, y agrega en un archivo el
        evento de la consulta.
        '''
        try:
            with connect(host=ArticleRepository.__host, database=ArticleRepository.__database, \
                         username=ArticleRepository.__username, password=ArticleRepository.__password) as connection:
                with connection.cursor() as cursor:

                    cursor.execute(ArticleRepository.__SELECT_CLOTHES_QUERY)

                    articles = cursor.fetchall()

                    self.__article_log.print(ArticleLog.events['QUERY'], articles)

                    return [ArticleClothesDetail(*article) for article in articles]
        except Error as error:
            Log.print(error)
            raise Exception("Ocurrió un error al realizar la consulta")


    def find_articles_by_accessories_category(self):
        '''
        Obtiene los artículos por categoría de accesorios
        de la base de datos, y agrega en un archivo el
        evento de la consulta.
        '''
        try:
            with connect(host=ArticleRepository.__host, database=ArticleRepository.__database, \
                         username=ArticleRepository.__username, password=ArticleRepository.__password) as connection:
                with connection.cursor() as cursor:

                    cursor.execute(ArticleRepository.__SELECT_ACCESSORIES_QUERY)

                    articles = cursor.fetchall()

                    self.__article_log.print(ArticleLog.events['QUERY'], articles)

                    return [ArticleAccessoryDetail(*article) for article in articles]

        except Error as error:
            Log.print(error)
            raise Exception("Ocurrió un error al realizar la consulta")


    def find_articles_by_shoes_category(self):
        '''
        Obtiene los artículos por categoría de calzado
        de la base de datos, y agrega en un archivo el
        evento de la consulta.
        '''
        try:
            with connect(host=ArticleRepository.__host, database=ArticleRepository.__database, \
                         username=ArticleRepository.__username, password=ArticleRepository.__password) as connection:
                with connection.cursor() as cursor:

                    cursor.execute(ArticleRepository.__SELECT_SHOES_QUERY)

                    articles = cursor.fetchall()

                    self.__article_log.print(ArticleLog.events['QUERY'], articles)

                    return [ArticleShoeDetail(*article) for article in articles]

        except Error as error:
            Log.print(error)
            raise Exception("Ocurrió un error al realizar la consulta")



'''
Clase que representa el guardado
de los eventos que ocurren en la
base de datos, en un archivo de 
texto.
'''
class ArticleLog:

    __filepath = "relaciones_de_tablas.txt"
    __encoding = "utf-8"

    events = {

        'ADD': 'ALTA',
        'UPDATE': 'MODIFICACIÓN',
        'DELETE': 'BAJA',
        'QUERY': 'CONSULTA'
    }

    def print(self, event, articles):
        '''
        Escribe en un archivo los eventos que
        se realicen sobre la base de datos,
        como consultas, altas, bajas, etc.
        '''
        with open(ArticleLog.__filepath, "at", encoding = ArticleLog.__encoding) as write_obj:
            for article in articles:
                print(f'{article} | {event} | {datetime.today()}', file = write_obj)