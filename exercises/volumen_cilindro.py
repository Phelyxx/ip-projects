# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:09:45 2020

@author: usuario
"""

def calcular_volumen_cilindro(radio: float, altura: float)->float:
    """ Volumen de un cilindro
    Parámetros:
      radio (float): Radio de la base del cilindro
      altura (float): Altura del cilindro
    Retorno:
      float: El volumen del cilindro readondeado a un decimal
    """
    pass
    volumen = 3.1416 * (radio ** 2) * altura
    return round(volumen, 1)
    