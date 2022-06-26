'''
Author: Joel Rubio
Date: 22-06-2022
'''

from datetime import datetime


'''
Clase que guarda los errores que
ocurran en el programa en un archivo
de texto
'''
class Log:
    
    __filepath = "logs.txt"
    __encoding = "utf-8"

    @staticmethod
    def print(text):
        '''
        Agrega el texto de error en un
        archivo de texto.
        '''
        with open(Log.__filepath, "at", encoding = Log.__encoding) as write_obj:
            print(f'{datetime.today()} - {text}', file = write_obj)