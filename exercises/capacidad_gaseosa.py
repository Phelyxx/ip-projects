# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 07:28:49 2020

@author: usuario
"""

def desperdicio_de_gaseosa(amigo_1: dict, amigo_2: dict, amigo_3: dict, capacidad_boton: float)->str:
    """ Ida al Cine
    Parámetros:
      amigo_1 (dict): Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str)
                      "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la
                      capacidad que ha sido llenada de su vaso hasta el momento (float)
      amigo_2 (dict): Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str)
                      "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la
                      capacidad que ha sido llenada de su vaso hasta el momento (float)
      amigo_3 (dict): Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str)
                      "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la
                      capacidad que ha sido llenada de su vaso hasta el momento (float)
      capacidad_boton (float): La cantidad de gaseosa que se servirá si los amigos deciden oprimir el botón
                               correspondiente.
    Retorno:
      str: El nombre del amigo a quien se le riega primero la gaseosa, suponiendo un orden ascendente en cuanto
           a que amigo llena primero su vaso. (Es decir, primero llena el amigo_1, luego el 2, luego el 3) Si a
           ningun amigo se le riega la gaseosa, retorne None. Si a más de un amigo se le riega la gaseosa,
           retorna el primero.
    """
    pass
    capacidad_actual1 = amigo_1.get("capacidad_actual")
    nombre_1 = amigo_1.get("nombre")
    capacidad_1 = amigo_1.get("capacidad_vaso")
    nombre_2 = amigo_2.get("nombre")
    capacidad_actual2 = amigo_2.get("capacidad_actual")
    capacidad_2 = amigo_2.get("capacidad_vaso")
    nombre_3 = amigo_3.get("nombre")
    capacidad_3 = amigo_3.get("capacidad_actual")
    capacidad_actual3 = amigo_3.get("capacidad_vaso")
    if capacidad_boton>(capacidad_1-capacidad_actual1):
        return nombre_1
    elif capacidad_boton>(capacidad_2-capacidad_actual2):
        return nombre_2
    elif capacidad_boton>(capacidad_actual3-capacidad_3):
        return nombre_3
    else:
        return None