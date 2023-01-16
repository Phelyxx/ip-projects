# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:20:55 2020

@author: usuario
"""

def clasificar_regalo(ide: int)->str:
    """ Regalo de Santa
    Parámetros:
      id (int): El identificador del regalo cuyo tipo de persona se quiere calcular.
    Retorno:
      str: Si el número es Palíndromo e impar, el regalo corresponde a una niña, y se retorna "girl" Si el
           número es Palíndromo y par, el regalo corresponde a un niño, y se retorna "boy" Si el número es par,
           pero no palíndromo, el regalo corresponde a un hombre, y se retorna "man" Si el número es impar,
           pero no palíndromo, el regalo corresponde a una mujer, y se retorna "woman"
    """
    pass
    ide_str = str(ide)
    invert = ide_str[::-1]
    par = ide % 2
    regalo = "woman"
    if invert == ide_str and par == 0:
       regalo = "boy"
    elif  invert == ide_str and par == 1:  
       regalo = "girl"
    elif  invert != ide_str and par == 0:  
       regalo = "man"
    return regalo
          
       
        