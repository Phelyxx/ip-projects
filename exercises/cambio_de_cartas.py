# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:30:42 2020

@author: usuario
"""

def cambio_de_cartas(carta_mano: dict, opcion_1: dict, opcion_2: dict)->int:
    """ Cartas
    Parámetros:
      carta_mano (dict): Carta que tiene en la mano. Tiene las llaves "numero" y "palo".
      opcion_1 (dict): Primera opción de robo. Tiene las llaves "numero" y "palo".
      opcion_2 (dict): Segunda opción de robo. Tiene las llaves "numero" y "palo".
    Retorno:
      int: Número de la carta que será robada para hacer trampa (1 o 2), o 0 si ninguna carta le ayuda.
    """
    pass
    robo_carta = 0
    if carta_mano["numero"] == opcion_1["numero"] or carta_mano["palo"] == opcion_1["palo"]:
       robo_carta = 1
    elif carta_mano["numero"] == opcion_2["numero"] or carta_mano["palo"] == opcion_2["palo"]:
       robo_carta = 2
    return robo_carta
   
     