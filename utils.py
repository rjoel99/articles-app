'''
Author: Joel Rubio
Date: 22-06-2022
'''

import os
import configparser


def from_config(file_name):
    '''
    Devuelve un objeto para obtener
    propiedades de un archivo de
    configuración.
    '''
    directory = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(directory, file_name)
    
    config = configparser.RawConfigParser()
    config.read(init_file)

    return config