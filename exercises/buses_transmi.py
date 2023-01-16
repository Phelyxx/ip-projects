# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:56:05 2020

@author: usuario
"""

def despacho_buses(personas_bus: int, personas_estacion: int)->bool:
    """ La estación de Transmilenio
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse
      personas_estacion (int): Número de personas esperando el bus en la estación
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """
    pass
    despacho = False
    if personas_bus > 150 or personas_estacion >=50: despacho = True
    return despacho  